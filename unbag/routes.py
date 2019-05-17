import config
from .models import Post, Event, Issue
from flask_security import current_user
from flask import Blueprint, send_from_directory, render_template, abort

bp = Blueprint('main', __name__)

@bp.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@bp.route('/')
def index():
    issues = Issue.query.filter(Issue.name!='Programs', Issue.published).order_by(Issue.id.asc()).all()
    return render_template('index.html', issues=issues, current_issue=issues[-1], current_post=Post.latest_event())

@bp.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(config.UPLOAD_FOLDER, filename)

@bp.route('/issue/<slug>')
def issue(slug):
    issue = Issue.query.filter_by(slug=slug).first_or_404()
    issues = Issue.query.filter(Issue.name!='Programs', Issue.published).order_by(Issue.id.desc()).all()
    return render_template('issue.html', issues=issues, current_issue=issue)

@bp.route('/<issue>/<slug>')
def post(issue, slug):
    post = Post.query.filter(Post.slug==slug, Post.issue.has(slug=issue)).first_or_404()
    if not post.published and not current_user.is_authenticated:
        abort(404)
    issues = Issue.query.filter(Issue.name!='Programs', Issue.published).order_by(Issue.id.desc()).all()
    return render_template('post.html', current_issue=post.issue, current_post=post, issues=issues)

@bp.route('/programs')
def events():
    events = [e.post for e in Event.query.order_by(Event.end.desc(), Event.start.asc()).all() if e.post.published]
    issues = Issue.query.filter(Issue.name!='Programs', Issue.published).order_by(Issue.id.desc()).all()
    issue = Issue.query.filter(Issue.name=='Programs').first()
    return render_template('events.html', events=events, current_issue=issue, issues=issues, current_post=Post.latest_event())

@bp.route('/donate')
def donate():
    issues = Issue.query.filter(Issue.name!='Programs', Issue.published).order_by(Issue.id.asc()).all()
    return render_template('donate.html', current_issue=issues[-1], issues=issues)

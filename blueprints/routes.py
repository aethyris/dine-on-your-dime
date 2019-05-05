@blueprints.route('/follow/<username>')
@login_required
def favorite(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot favorite yourself!')
        return redirect(url_for('user', username=username))
    current_user.favorite(user)
    db.session.commit()
    flash('You are favoriteing {}!'.format(username))
    return redirect(url_for('user', username=username))

@blueprints.route('/like/<username>')
@login_required
def like(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot like yourself!')
        return redirect(url_for('user', username=username))
    current_user.like(user)
    db.session.commit()
    flash('You are  liing {}.'.format(username))
    return redirect(url_for('user', username=username))

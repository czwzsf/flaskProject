import hashlib

from flask import Blueprint, render_template, request, redirect, url_for

from apps.user.models import User, UserRoot, Mis
from exts import db

user_bp = Blueprint('user', __name__)  # 这个时候起的蓝图的名称是为后来url_for的时候来使用的


# 首页界面
@user_bp.route('/', methods=['POST', 'GET'])
def user_first():
    return render_template('user/first.html')


# 注册界面
@user_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # 读取网页数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        # 当两次输入密码正确时，进入数据库数据存储模块
        if password == repassword:
            # 讲User模型的多个数据赋予user
            user = User()
            # 讲UserRoot模型的多个数据赋予user_root
            user_root = UserRoot()
            user.username = username
            # 加密用户输入的密码
            user.password = hashlib.sha1(password.encode('utf-8')).hexdigest()
            user.phone = phone
            user.email = email
            user_root.username = username
            # 管理员账号所获取的密码不加密
            user_root.password = password
            user_root.email = email
            user_root.phone = phone
            # 添加并提交
            db.session.add(user)
            db.session.add(user_root)
            db.session.commit()
            return redirect(url_for('user.user_center'))
    else:
        return render_template('user/register.html')


# 用户中心
@user_bp.route('/user_center', methods=['POST', 'GET'])
def user_center():
    # 查询数据库中的数据
    users = User.query.all()
    return render_template('user/center.html', users=users)


@user_bp.route('/user_center_MIS', methods=['POST', 'GET'])
def user_center_MIS():
    data_MIS = Mis.query.all()
    return render_template('user/center_1.html', data_MIS=data_MIS)


# 登陆界面
@user_bp.route('/login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 关键处用来查找用户名与其对应的密码
        new_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
        user_list = User.query.filter_by(username=username)
        for user in user_list:
            print(user)
            if user.password == new_password:
                return '用户登入成功'
        else:
            return render_template('user/login.html', msg='用户名或密码错误')
    return render_template('user/login.html')

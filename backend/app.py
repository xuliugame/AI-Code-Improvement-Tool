# 导入必要的库和模块
from dotenv import load_dotenv
load_dotenv()  # 加载环境变量
from flask import Flask, jsonify
from flask_cors import CORS  # 用于处理跨域请求
from user.models import db  # 数据库模型
from user.user import auth_bp  # 用户认证蓝图
from api.openai_api import api_bp  # OpenAI API蓝图
from config import Config  # 应用配置
import os
from flask_jwt_extended import JWTManager  # JWT认证管理

# 创建Flask应用实例
app = Flask(__name__)
app.config.from_object(Config)  # 加载配置

# JWT配置
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-jwt-secret')  # JWT密钥
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # Token有效期1小时
app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Token位置
app.config['JWT_HEADER_NAME'] = 'Authorization'  # Token头名称
app.config['JWT_HEADER_TYPE'] = 'Bearer'  # Token类型

CORS(app)  # 启用跨域支持
db.init_app(app)  # 初始化数据库

# 初始化JWT管理器
jwt = JWTManager(app)

# Token过期回调函数
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token has expired',
        'error': 'token_expired'
    }), 401

# 无效Token回调函数
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Invalid token',
        'error': str(error)
    }), 401

# 未授权访问回调函数
@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify({
        'message': 'Missing Authorization Header',
        'error': str(error)
    }), 401

# Token需要刷新回调函数
@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token is not fresh',
        'error': 'fresh_token_required'
    }), 401

# 注册蓝图
app.register_blueprint(auth_bp)  # 注册用户认证蓝图
app.register_blueprint(api_bp)  # 注册API蓝图

# 健康检查路由
@app.route("/")
def health_check():
    return "OK", 200

# 主程序入口
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建数据库表
    app.run(debug=True)  # 启动应用，开启调试模式





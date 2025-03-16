from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

# تعريف قاعدة البيانات
Base = declarative_base()

# تعريف جدول المحادثات (Conversation)
class Conversation(Base):
    __tablename__ = 'conversations'
    
    id = Column(Integer, primary_key=True)  # معرف المحادثة
    user_id = Column(Integer, ForeignKey('users.id'))  # معرف المستخدم (مفتاح خارجي)
    timestamp = Column(DateTime, default=func.now())  # تاريخ ووقت إنشاء المحادثة
    
    # العلاقة مع جدول الرسائل (Message)
    messages = relationship('Message', back_populates='conversation')

# تعريف جدول الرسائل (Message)
class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)  # معرف الرسالة
    conversation_id = Column(Integer, ForeignKey('conversations.id'))  # معرف المحادثة (مفتاح خارجي)
    text = Column(Text)  # نص الرسالة
    sender = Column(String)  # المرسل (مستخدم أو نظام)
    timestamp = Column(DateTime, default=func.now())  # تاريخ ووقت إرسال الرسالة
    
    # العلاقة مع جدول المحادثات (Conversation)
    conversation = relationship('Conversation', back_populates='messages')

def init_db(engine):
    """تهيئة قاعدة البيانات وإنشاء الجداول"""
    Base.metadata.create_all(engine)

def create_session(engine):
    """إنشاء جلسة جديدة"""
    Session = sessionmaker(bind=engine)
    return Session()

def add_conversation(session, user_id):
    """إضافة محادثة جديدة"""
    new_conversation = Conversation(user_id=user_id)
    session.add(new_conversation)
    session.commit()
    return new_conversation

def add_message(session, conversation_id, text, sender):
    """إضافة رسالة جديدة إلى محادثة"""
    new_message = Message(conversation_id=conversation_id, text=text, sender=sender)
    session.add(new_message)
    session.commit()

def get_conversations(session):
    """جلب جميع المحادثات والرسائل"""
    conversations = session.query(Conversation).all()
    for conv in conversations:
        print(f"Conversation ID: {conv.id}, User ID: {conv.user_id}, Timestamp: {conv.timestamp}")
        for msg in conv.messages:
            print(f"  Message: {msg.text}, Sender: {msg.sender}, Timestamp: {msg.timestamp}")

if __name__ == "__main__":
    # إنشاء محرك قاعدة البيانات (SQLite في هذا المثال)
    engine = create_engine('sqlite:///knowledge.db')
    
    # تهيئة قاعدة البيانات
    init_db(engine)
    
    # إنشاء جلسة
    session = create_session(engine)
    
    # إضافة محادثة جديدة
    new_conversation = add_conversation(session, user_id=1)
    
    # إضافة رسالة إلى المحادثة
    add_message(session, conversation_id=new_conversation.id, text="Hello, World!", sender="user")
    
    # جلب المحادثات والرسائل
    get_conversations(session)

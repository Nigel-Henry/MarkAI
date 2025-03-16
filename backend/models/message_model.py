from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.sql import func

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
    text = Column(Text, nullable=False)  # نص الرسالة (غير مسموح بقيم فارغة)
    sender = Column(String(50), nullable=False)  # المرسل (مستخدم أو نظام)
    timestamp = Column(DateTime, default=func.now())  # تاريخ ووقت إرسال الرسالة (يتم تعيينه تلقائيًا)
    
    # العلاقة مع جدول المحادثات (Conversation)
    conversation = relationship('Conversation', back_populates='messages')

# إنشاء محرك قاعدة البيانات (SQLite في هذا المثال)
engine = create_engine('sqlite:///knowledge.db')

# إنشاء الجلسة
Session = sessionmaker(bind=engine)
session = Session()

# إنشاء جميع الجداول في قاعدة البيانات
Base.metadata.create_all(engine)

# إنشاء محادثة جديدة
new_conversation = Conversation(user_id=1)
session.add(new_conversation)
session.commit()

# إضافة رسالة إلى المحادثة
new_message = Message(conversation_id=new_conversation.id, text="Hello, World!", sender="user")
session.add(new_message)
session.commit()

# جلب المحادثات والرسائل
conversations = session.query(Conversation).all()
for conv in conversations:
    print(f"Conversation ID: {conv.id}, User ID: {conv.user_id}, Timestamp: {conv.timestamp}")
    for msg in conv.messages:
        print(f"  Message: {msg.text}, Sender: {msg.sender}, Timestamp: {msg.timestamp}")
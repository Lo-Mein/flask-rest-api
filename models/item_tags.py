from db import db


class ItemTags(db.Model):
    __tablename__ = "item_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), nullable=False)

    # store = db.relationship("StoreModel", back_populates="tags")
    # item = db.relationship("ItemModel", back_populates="tags", secondary="item_tags")
    

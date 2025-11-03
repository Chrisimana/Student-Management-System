import json
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_file="students_data.json"):
        self.db_file = db_file
        self.ensure_database_exists()
    
    def ensure_database_exists(self):
        """Ensure database file exists"""
        if not os.path.exists(self.db_file):
            self.init_database()
    
    def init_database(self):
        """Initialize empty database"""
        with open(self.db_file, 'w') as file:
            json.dump([], file)
    
    def load_data(self):
        """Load all data from database"""
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except:
            return []
    
    def save_data(self, data):
        """Save data to database"""
        with open(self.db_file, 'w') as file:
            json.dump(data, file, indent=4)
    
    def add_record(self, record):
        """Add new record to database"""
        data = self.load_data()
        record['id'] = len(data) + 1
        record['created_at'] = datetime.now().isoformat()
        data.append(record)
        self.save_data(data)
        return record
    
    def delete_record(self, record_id):
        """Delete record by ID"""
        data = self.load_data()
        data = [record for record in data if record['id'] != record_id]
        self.save_data(data)
        return len(data)
    
    def search_records(self, query):
        """Search records by query"""
        data = self.load_data()
        if not query:
            return data
        
        results = []
        for record in data:
            if (query.lower() in record.get('name', '').lower() or 
                query.lower() in record.get('nim', '').lower()):
                results.append(record)
        return results
class Video:
    
    def __init__(self, name, course, url, desc):
        self.name = name
        self.course = course
        self.url = url
        self.desc = desc
        
    def get_staff(self, *args):
        z = []
        if name in args:
            z.append(self.name)
        if course in args:
            z.append(self.course)        
        if url in args:
            z.append(self.url)     
        if desc in args:
            z.append(self.desc)  
        return z
    
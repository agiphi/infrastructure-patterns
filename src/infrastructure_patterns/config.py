import os
def config(): return {"environment":os.getenv("APP_ENV","development"),"port":int(os.getenv("PORT","8080"))}

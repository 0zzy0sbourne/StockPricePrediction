
from flask import render_template , request , redirect , url_for , Flask , Response   , make_response 
from io import StringIO
import sys
import random
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy 
from sqlalchemy import create_engine ,MetaData
import config
import matplotlib.pyplot as plt
import ml 
from ml import plotSaveData , plotEthereum , rippleDataFrame
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure 
#from matplotlib.backends.backend_agg import FigureCanvasAgg 
#from matplotlib.backends.backend_svg import FigureCanvasSVG
# from matplotlib.figure import Figure 
#sys.path.append
 # import ml , scraping from this data file . 
#sys.path.append('/home/Desktop/python/venv/application/data')

 #import scraping




app = Flask(__name__ , static_url_path='/static')
# tell flask app where our database will be stored : 

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////tmp/test.db'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 300 
app.config['SQLALCHEMY_ECHO'] = True # If set to True SQLAlchemy will log all the statements issued to stderr which can be useful for debugging.
app.config['SQLALCHEMY_POOL_TIMEOUT'] =  10 # Specifies the connection timeout in seconds for the pool.
convention = { # put the metadata conventions here .  

}
metadata = MetaData(naming_convention = convention)
db = SQLAlchemy(app ,metadata = metadata)

class Coin(db.Model): # can save the infos about the coins like png's 
    __tablename__  = 'coins'
    id = db.Column(db.Integer , primary_key = True)
    coinName = db.Column(db.String(20)  , primary_key= False , nullable = False )

class Member(db.Model): 
    __tablename__ = "member"
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(20) , primary_key = False   , nullable = False )
    email= db.relationship("Address"  , backref = 'member' , lazy = True)
    def __repr__(self): 
        return  '<Member %r>' % self.name

class Comment(db.Model): 
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    content= db.Column(db.String(140)  , primary_key = False)
    author = db.relationship("Member" , backref = 'comments' , lazy=True) 
    
class Address(db.Model): 
    __tablename__ = "address"
    email = db.Column(db.String(30) , primary_key =True , nullable = False)
    person_id = db.Column(db.Integer,db.ForeignKey('member.id') , nullable = False)
    def __init__(self , email , person_id): 
        self.email = email 
        self.person_id = person_id




@app.route('/ripple.png')
def ripple_png():
    output = io.BytesIO()
    FigureCanvas(ripplePriceFig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')







@app.route('/')
def mainpage(): 


    

    return render_template('mainpage.html'  )
    



@app.route('/mainpage/bitcoin')
def bitcoin() : 

    

    return render_template('bitcoin.html')


@app.route('/mainpage/ethereum')
def ethereum(): 
    '''
    plt.scatter(ethx, ethy)
    ethereum_fig = plt.figure()
    ethereum_html_graph = mpld3.fig_to_html(ethereum_fig)
    '''
    return render_template('ethereum.html' )


@app.route('/mainpage/tether')
def tether(): 

    return render_template('tether.html')


@app.route('/mainpage/ripple')
def ripple():
    figList = plotSaveData(rippleDataFrame , 'Ripple')
    priceFig = figList[0]
    volumeFig = figList[1]
    canvasPrice = FigureCanvas(priceFig)
    canvasVolume = FigureCanvas(volumeFig)
    outputPrice = StringIO()
    outputVolume = StringIO()
    canvasPrice.print_png(outputPrice)
    canvasVolume.print_png(outputVolume)
    responsePrice = make_response(outputPrice.getvalue())
    responseVolume = make_response(outputVolume.getvalue())
    responsePrice.mimetype = 'image/png'
    responseVolume.mimetype = 'image/png'
    return render_template('ripple.html')
    #####################################ERROR##########################################
    #string argument expected , got bytes .
    #Plot a PNG using matplotlib in a web request, using Flask. 
    
    

@app.route('/mainpage/bitcash')
def bitcash(): 

    return render_template('bitcash.html')












if __name__ == "__main__" : 
    app.run(host=os.getenv('IP', '0.0.0.0'), 
    port=int(os.getenv('PORT', 4444)))

#app.run(debug=True)



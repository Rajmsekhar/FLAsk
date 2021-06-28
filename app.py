from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        try:
            num1=int(request.form['num1'])
            num2 = int(request.form['num2'])
        except Exception as error :
            result = str (error)
            return result

        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        if (operation == 'square'):
            r = num1 ** num2
            result = 'the quotient when ' + str(num1) + ' is powered by ' + str(num2) + ' is ' + str(r)
        if (operation == 'square root') and num2 == 2:
            try:
                r = num1 ** (1/num2)
                result = 'the quotient when ' + str(num1) + ' is square route ' + str(num2) + ' is ' + str(r)
            except:
                raise error(True, "2 is not perfect square")
                return result
            finally:
                print("try except & finally block")


        if (operation == 'cuberoot'):
               r = int(round(num1 ** 1/num2))
               result = 'the quotient when ' + str(num1) + ' is cube route ' + str(num2) + ' is ' + str(r)
        if (operation == 'mod'):
            r = num1 % num2
            result = 'the quotient when ' + str(num1) + ' is Mod of' + str(num2) + ' is ' + str(r)



        #return render_template('results.html',result=result)

    return render_template('results.html', result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        if (operation == 'square'):
            r = num1 ** num2
            result = 'the quotient when ' + str(num1) + ' is powered by ' + str(num2) + ' is ' + str(r)
        if (operation == 'square root') and num2 == 2:
            try:
               r = num1 ** (1/num2)
               result = 'the quotient when ' + str(num1) + ' is square route ' + str(num2) + ' is ' + str(r)
            except:
               raise error(True,"2 is not perfect square" )
               return result
        if (operation == 'cuberoot'):
               r = int(round(num1 ** 1/num2))
               result = 'the quotient when ' + str(num1) + ' is cube route ' + str(num2) + ' is ' + str(r)
               return result
        if (operation == 'mod'):
            r = num1 % num2
            result = 'the quotient when ' + str(num1) + ' is mod of ' + str(num2) + ' is ' + str(r)


        return jsonify(result)


if __name__ == '__main__':
    app.run()

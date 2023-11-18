import matplotlib.pyplot as plot;
import math;


#Problem 1
def S(x,n):
    result = float(0);
    denominator = float(1);

    for i in range(0,n):
        term = float(pow(x,i) / denominator);
        #print("iteration: {} has term: {}".format(i,term));

        result += term;

        denominator = float(denominator * (i+1));


    return result;

def Question_1_part_3():
    x_coordinates = [];
    y_coordinates = [];
    x = -20;
    n = 101;

    for i in range(0,n):
        x_coordinates.append(i);
        relative_Error = math.log10(abs(S(x,i) - math.exp(x))/math.exp(x));
        y_coordinates.append(relative_Error);
        #print("iteration: {} | Error: {}").format( i, relative_Error);
    
    print("Approximation: {} | vs | Expected: {}".format(S(x,n),20, math.exp(-20)))

    plot.scatter(x_coordinates,y_coordinates);
    plot.title("Relative Error Computing first 100 iterations of e^-20 using Taylor Series");
    plot.xlabel("Iteration N");
    plot.ylabel("Relative Error");
    plot.xlim(0,n);

    plot.show();

#Problem 2
#part 1
def d_c(f,x,h):
    return (f(x+h)-f(x-h))/(2*h);

#part 2
def g(x):
    return 1/(1+pow(x,2));

#part 3
def e_c(f,h,x = 1):
    return abs(d_c(f,x,h) - .5);

def Question_2_part_3():
    #part 3
    h_values = [pow(2,-x) for x in range(1,16)];

    x_coordinates = [math.log10(h) for h in h_values];
    print(x_coordinates)

    y_coordinates = [math.log10( e_c( g , h ) ) for h in h_values]

    plot.scatter(x_coordinates,y_coordinates);
    plot.xlabel("log_10(h)");
    plot.ylabel("Absolute error")
    plot.title("Absolute error of central difference scheme as h decreases")

    plot.show();

def Question_2_part_4():
    k_values = [x for x in range(0,15)];

    array_of_slopes = [(math.log10(e_c(g,pow(2,(-k)-1)))-math.log10(e_c(g,pow(2,-k))))/(math.log10(pow(2,(-k)-1)) - math.log10(pow(2,-k))) for k in k_values]

    plot.scatter(k_values,array_of_slopes);

    plot.xlabel('k');
    plot.ylabel('slopes of consecutive points')
    plot.title('Sumthin');

    plot.show();

    
    


if __name__ == '__main__':

    Question_2_part_4();



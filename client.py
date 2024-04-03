import requests
import json
import random


#Main function 
if __name__ == "__main__":

    ######1######

    # Pull the list of regions. Print the regions list on the console (at this stage, it should have default initial values).
    res = requests.get('http://127.0.0.1:5000/election/regions')
    response = json.loads(res.text)
    print("BULLET 1 :Initial Election Regions:", response)
    print("\n")

    ######2######

    # Add a new region called ”METU” and ”EEE” with 10 and 3 seats, respectively.
    metudata = {"region_name": "METU", "number_of_seats": 100}
    eeedata = {"region_name": "EEE", "number_of_seats": 3}
    # PUT request to add the new region
    res = requests.put('http://127.0.0.1:5000/election/regions', json=metudata)
    res = requests.put('http://127.0.0.1:5000/election/regions', json=eeedata)
    # GET request to retrieve updated election regions
    res = requests.get('http://127.0.0.1:5000/election/regions')
    response = json.loads(res.text)
    print("BULLET 2 :Election Regions with METU and EEE:", response)
    print("\n")

    ######3######

    #Try to re-add ”METU” and print the error message and status code.
    res = requests.put('http://127.0.0.1:5000/election/regions', json=metudata)
    print("BULLET 3: Status Code:", res.status_code) #406
    print("BULLET 3: Error message:", res.text)
    print("\n")

    ######4######

    #Delete ”EEE” from the region list.
    res = requests.delete('http://127.0.0.1:5000/election/regions', json=eeedata)
    res = requests.get('http://127.0.0.1:5000/election/regions')
    response = json.loads(res.text)
    print("BULLET 4: Updated Election Regions without EEE:", response)
    print("\n")

    ######5######

    #Pull the list of the parties currently in the list. Print the party list on the console (at
    #this stage, it should be empty).
    res = requests.get('http://127.0.0.1:5000/election/parties')
    response = json.loads(res.text)
    print("BULLET 5: Initial Parties :", response)
    print("\n")

    ######6######

    #Add ”Party1”, ”Party2”, ”Party3” and ”Party4” to the list by using PUT method.
    party1 = {"party_name": "Party1"}
    party2 = {"party_name": "Party2"}
    party3 = {"party_name": "Party3"}
    party4 = {"party_name": "Party4"}

    res = requests.put('http://127.0.0.1:5000/election/parties', json=party1)
    res = requests.put('http://127.0.0.1:5000/election/parties', json=party2)
    res = requests.put('http://127.0.0.1:5000/election/parties', json=party3)
    res = requests.put('http://127.0.0.1:5000/election/parties', json=party4)

    ######7######

    #Print the list of the parties by re-fetching the data.
    res = requests.get('http://127.0.0.1:5000/election/parties')
    response = json.loads(res.text)
    print("BULLET 7: parties added:", response)
    print("\n")
    ######8######

    #Try to re-add ”Party4” and print the error message and status code.
    party4={"party_name": "Party4"}
    res = requests.put('http://127.0.0.1:5000/election/parties', json=party4)
    
    print("BULLET 8: Status Code:", res.status_code) #406
    print("BULLET 8: Error message:", res.text)
    
    print("\n")
    ######9######

    #Delete ”Party4” from the party list
    res = requests.delete('http://127.0.0.1:5000/election/parties', json=party4)

    ######10######

    #Print the remaining parties.
    res = requests.get('http://127.0.0.1:5000/election/parties')
    response = json.loads(res.text)
    print("BULLET 10: Remaining Parties:", response)
    print("\n")

    #D’Hondt simulation 
    res = requests.get('http://127.0.0.1:5000/election/regions')
    response = json.loads(res.text)

    selected_regions = random.sample(response, 3) #3 random regions selected

    for region in selected_regions:
        votepercentage = {}
        
        votepercentage[f"Party{1}"] = 60
        votepercentage[f"Party{2}"] = 20
        votepercentage[f"Party{3}"] = 20  

        data = {"region": region["region_name"], **votepercentage}

        # Send POST request for simulation
        response = requests.post('http://127.0.0.1:5000/election/simulate', json=data)

        # Print the resulting MP distribution
        
        print(f"MP distribution for {region['region_name']}:", response.json())
        print("\n")
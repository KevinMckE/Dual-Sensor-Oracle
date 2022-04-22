pragma solidity 0.8.7;
//"SPDX-License-Identifier: MIT"

contract StoreData {
    
    string public data;

    function set(string memory _data) external {
        data = _data;
    }

    function get() external view returns (string memory){
        return data;
    }

}
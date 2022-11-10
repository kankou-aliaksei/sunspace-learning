// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Rating {
    struct Entity {
        uint32 id;
        bytes32 name;
        uint256 totalRating;
        uint16 ratersNumber;
    }

    struct Rater {
        mapping(uint32 => bool) ratedEntities;
    }

    Entity[] private entities;
    mapping(address => Rater) raters;

    function rate(uint32 _entityId, uint8 _rating) external {
        require(entities.length > _entityId, "Entity not found");

        if (raters[msg.sender].ratedEntities[_entityId] == true) {
            return;
        }

        entities[_entityId].totalRating += _rating;
        entities[_entityId].ratersNumber ++;
        raters[msg.sender].ratedEntities[_entityId] = true;
    }

    function getEntry(uint32 _id) external view returns (Entity memory) {
        return entities[_id];
    }

    function createEntity(bytes32 _name) external {
        Entity memory entity = Entity({
            id: uint32(entities.length),
            name: _name,
            totalRating: 0,
            ratersNumber: 0
        });

        entities.push(entity);
    }
}
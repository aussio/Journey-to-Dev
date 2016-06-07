require "./ex47-Room.rb"
require "minitest/autorun"

class TestGame < MiniTest::Unit::TestCase

    def setup
        @room = Room.new("Gold Room", 
                        """This room has gold within it!
                        You can grab the gold if you dare...
                        and there's a door to the North.""")
    end

    def test_room_init
        assert_equal "Gold Room", @room.name
        assert_equal """This room has gold within it!
                        You can grab the gold if you dare...
                        and there's a door to the North.""", @room.description
    end

    def test_room_paths
        rooms ={}
        ['Center', 'North', 'South'].each do |dir|
            rooms[dir] = Room.new(dir, "Room to the #{dir}")
        end
        @room.add_paths(rooms)
        assert_equal(rooms['North'], @room.go('North'))
        assert_equal(rooms['South'], @room.go('South'))
    end

end

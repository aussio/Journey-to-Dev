require 'minitest/autorun'
require './sticker.rb'

class TestSticker < MiniTest::Unit::TestCase

    # Tests for make_counter
    data_provider = {'wpengine' => {'w' => 1, 'p' => 1, 'e' => 2, 'n' => 2, 'g' => 1, 'i' => 1},
                     'winning' => {'w' => 1, 'i' => 2, 'n' => 3, 'g' => 1},
                     'zzzzz' => {'z' => 5}
                    }    
    data_provider.each do |word, hash|
        define_method("test_#{word}_counter") do
            assert_equal(hash, make_counter(word))
        end
    end

    # Tests for number_of_stickers_required
    data_provider = {'wpengine' => 1,
                     'winning' => 2,
                     'wwwww' => 5,
                     'zzz' => -1,
                     'new' => 1
                    }
    data_provider.each do |word, num_stickers|
        define_method("test_#{word}_stickers") do
            assert_equal(num_stickers, number_of_stickers_required(word))
        end
    end
       
    # Tests for empty_of_letters?
    data_provider = [{:hash => {'w' => 1, 'p' => 1, 'e' => 2, 'n' => 2, 'g' => 1, 'i' => 1}, :bool => false},
                     {:hash => {'g' => 1, 'a' => 0, 'b' => -1}, :bool => false},
                     {:hash => {'z' => 0, 'a' => -1}, :bool => true}
                    ]
    count = 0
    data_provider.each do |data|
        define_method("test_#{count}_empty") do
            assert_equal(empty_of_letters?(data[:hash]), data[:bool])
        end
        count += 1
    end

    def test_hash_subtract
        hash1 = {'a' => 2, 'b' => 0, 'c' => 1}
        hash2 = {'a' => 1, 'b' => 2}
        subtracted_hash1 = hash_value_subtract(hash1, hash2)
        expected_hash = {'a' => 1, 'b' => -2, 'c' => 1}
        assert_equal(expected_hash, subtracted_hash1)
    end

end

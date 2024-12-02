import Data.List (sort)
import qualified Data.Text as T
import System.IO

pairUp xs ys = zipWith (\x y -> abs(x-y)) (sort xs) (sort ys)

main = do
    contents <- readFile "input.txt"

    --extract rows as list
    let rows = map (T.splitOn (T.pack "   ") . T.pack) (lines contents)

    --put into tuples and convert to Int
    let tuples = map (\x -> (read (T.unpack (x !! 0)) :: Int, read(T.unpack(x !! 1)) :: Int)) rows

    --unzip into seperate lists
    let (xs, ys) = unzip tuples

    print (sum (pairUp xs ys))
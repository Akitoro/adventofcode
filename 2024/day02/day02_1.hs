import System.IO ()
import qualified Data.Text as T


isSorted :: Ord b => (b -> b -> Bool) -> [b] -> Bool
isSorted ord xs  = (all (uncurry ord) . zip xs) $ tail xs
isDistance xs = all (\(a, b) -> abs(a-b) <= 3 && abs(a-b) >= 1) (zipAdj xs)

zipAdj xs = zip xs $ tail xs
main = do
    contents <- readFile "input.txt"

    let rows = map (T.splitOn (T.pack "   ") . T.pack) (lines contents)

    let tuples = map (T.splitOn (T.pack " ") . head) rows

    let numbers = map (map (\x -> read (T.unpack x) ::Int)) tuples

    let matching = map (\n -> (isSorted (<) n || isSorted (>) n) && isDistance n) numbers
    let total = length $ filter id matching
    print total


from models.LinkedList import LinkedList

def main():
    lista_liagda = LinkedList()
    while True:
        try:
            comandos: list = input().split(" ")
        except EOFError:
            return
        match comandos[0].upper():
            case "RPI":
                lista_liagda.insert_at_start(comandos[1])
                lista_liagda.traverse_list()
            case "RPF":
                lista_liagda.insert_at_end(comandos[1])
                lista_liagda.traverse_list()
            case "RPDE":
                lista_liagda.insert_after_item(comandos[2], comandos[1])
                lista_liagda.traverse_list()
            case "RPAE":
                lista_liagda.insert_before_item(comandos[2], comandos[1])
                lista_liagda.traverse_list()
            case "RPII":
                lista_liagda.insert_at_index( int(comandos[2]),comandos[1])
                lista_liagda.traverse_list()
            case "VNE":
                print(f"O número de elementos são {lista_liagda.get_count()}.")
            case "VP":
                if lista_liagda.search_item( comandos[1]):
                    print(f"O país {comandos[1]} encontra-se na lista.")
                else:
                    print(f"O país {comandos[1]} não se encontra na lista.")
            case "EPE":
                first_country = lista_liagda.start_node.item
                lista_liagda.delete_at_start()
                print(f"O país {first_country} foi eliminado da lista.")
            case "EUE":
                last_country = lista_liagda.get_last_node()
                lista_liagda.delete_at_end()
                print(f"O país {last_country} foi eliminado da lista.")
            case "EP":
                if lista_liagda.search_item(comandos[1]):
                    lista_liagda.delete_element_by_value(comandos[1])
                    print(f"O país {comandos[1]} foi eliminado da lista.")
                else:
                    print(f"O país {comandos[1]} não se encontra na lista.")
            case _:
                pass
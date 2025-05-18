import base64
from google.protobuf import descriptor_pb2, descriptor_pool, message_factory

"""

INFO


"""


class Get_link_google:
    
    def define_protobuf_classes(self):
        file_desc = descriptor_pb2.FileDescriptorProto()
        file_desc.name = "flights.proto"
        file_desc.package = "flights"

        # Airport message
        airport_msg = file_desc.message_type.add()
        airport_msg.name = "Airport"
        airport_field = airport_msg.field.add()
        airport_field.name = "airport"
        airport_field.number = 2
        airport_field.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
        airport_field.type = descriptor_pb2.FieldDescriptorProto.TYPE_STRING

        # FlightData message
        flight_msg = file_desc.message_type.add()
        flight_msg.name = "FlightData"

        flight_date = flight_msg.field.add()
        flight_date.name = "date"
        flight_date.number = 2
        flight_date.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
        flight_date.type = descriptor_pb2.FieldDescriptorProto.TYPE_STRING

        flight_from = flight_msg.field.add()
        flight_from.name = "from_flight"
        flight_from.number = 13
        flight_from.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
        flight_from.type = descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE
        flight_from.type_name = ".flights.Airport"

        flight_to = flight_msg.field.add()
        flight_to.name = "to_flight"
        flight_to.number = 14
        flight_to.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
        flight_to.type = descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE
        flight_to.type_name = ".flights.Airport"

        # Info message
        info_msg = file_desc.message_type.add()
        info_msg.name = "Info"

        info_data = info_msg.field.add()
        info_data.name = "data"
        info_data.number = 3
        info_data.label = descriptor_pb2.FieldDescriptorProto.LABEL_REPEATED
        info_data.type = descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE
        info_data.type_name = ".flights.FlightData"

        info_seed_a = info_msg.field.add()
        info_seed_a.name = "seed_a"
        info_seed_a.number = 19
        info_seed_a.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
        info_seed_a.type = descriptor_pb2.FieldDescriptorProto.TYPE_UINT32

        info_seed_b = info_msg.field.add()
        info_seed_b.name = "seed_b"
        info_seed_b.number = 20
        info_seed_b.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
        info_seed_b.type = descriptor_pb2.FieldDescriptorProto.TYPE_SINT32

        pool = descriptor_pool.DescriptorPool()
        pool.Add(file_desc)

        messages = message_factory.GetMessages([file_desc])
        return messages["flights.Info"], messages["flights.FlightData"], messages["flights.Airport"]

    def generate_tfs(self, departure_airport, arrival_airport, departure_date, return_date=None):
        Info, FlightData, Airport = self.define_protobuf_classes()
        
        info = Info()
        if return_date:
            info.seed_a = 1
            info.seed_b = -1
        else:
            info.seed_a = 2
            info.seed_b = 1

        # Outbound
        outbound = info.data.add()
        outbound.date = departure_date
        outbound.from_flight.CopyFrom(Airport(airport=departure_airport))
        outbound.to_flight.CopyFrom(Airport(airport=arrival_airport))

        # Return
        if return_date:
            inbound = info.data.add()
            inbound.date = return_date
            inbound.from_flight.CopyFrom(Airport(airport=arrival_airport))
            inbound.to_flight.CopyFrom(Airport(airport=departure_airport))

        binary_data = info.SerializeToString()
        return base64.urlsafe_b64encode(binary_data).decode("utf-8").rstrip("=")

    def generate_flights_url(self, tfs, lang="pl"):
        return f"https://www.google.com/travel/flights/search?tfs={tfs}&hl={lang}"

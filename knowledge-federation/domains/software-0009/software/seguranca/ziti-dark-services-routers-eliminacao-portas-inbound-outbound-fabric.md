---
id: software.seguranca.tranche04.000302
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/openziti/ziti/release-next/README.md", "https://netfoundry.io/docs/openziti/intro/", "https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenZiti: Dark Services e Dark Routers sem Portas de Escuta Inbound Expostas

## Em uma frase
Serviços e roteadores *dark* no OpenZiti operam sem abrir portas TCP/UDP de entrada (*inbound*) na internet ou na rede privada, iniciando apenas conexões de saída (*outbound*) autenticadas contra a malha.

## Por que importa
Ao eliminar portas de escuta públicas, atacantes externos não conseguem realizar *port scanning*, explorar vulnerabilidades pré-autenticação em listeners HTTP/SSH ou descobrir a existência do serviço.

## Como funciona
O servidor da aplicação (com SDK embutido ou *tunneler* colocalizado) conecta-se proativamente aos *Edge Routers* realizando uma operação de `Bind` autenticada por certificado X.509. Quando um cliente autorizado solicita `Dial` para o serviço lógico, a malha OpenZiti encaminha o fluxo até a conexão *outbound* já estabelecida pelo hospedeiro.

## Exemplo
```bash
# Verificar no host do serviço que não há porta aberta externamente além de loopback
ss -tulnp | grep 8443
# LISTEN 0 4096 127.0.0.1:8443 0.0.0.0:* users:(("internal-api",pid=2410,fd=7))

# Verificar terminators registrados no OpenZiti apontando para o serviço dark
ziti edge list terminators 'service.name="internal-orders-api"'
```

## Limites e trade-offs
Pelo menos um conjunto de *Edge Routers* de trânsito precisa ser alcançável tanto pelos clientes quanto pelos *Dark Routers*/serviços privados (geralmente em DMZ ou nuvem com porta 443 *outbound* liberada nos firewalls internos).

## Como verificar
Consulte `ziti edge list terminators` e confirme a presença de *terminators* dinâmicos ativos mesmo com regras de firewall bloqueando 100% de conexões de entrada (`INPUT DROP`) no servidor da aplicação.

## Conexões
- [[ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge]] — Veja também: OpenZiti: Arquitetura da Malha Zero Trust com Controller, Fabric Mesh e Edge Components.
- [[ziti-identities-enrollment-jwt-ott-certificados-x509-mutuos]] — Veja também: OpenZiti: Identidades, Enrollment via One-Time Token (OTT) JWT e mTLS X.509.
- [[ziti-sdks-application-embedded-zero-trust-go-c-python-jvm]] — Referência cruzada direta com ziti-sdks-application-embedded-zero-trust-go-c-python-jvm.
- [[ziti-tunnelers-ziti-edge-tunnel-intercept-host-tproxy-dns]] — Referência cruzada direta com ziti-tunnelers-ziti-edge-tunnel-intercept-host-tproxy-dns.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.

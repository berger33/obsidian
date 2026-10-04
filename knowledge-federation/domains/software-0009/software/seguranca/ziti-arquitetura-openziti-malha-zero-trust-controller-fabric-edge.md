---
id: software.seguranca.tranche04.000301
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

# OpenZiti: Arquitetura da Malha Zero Trust com Controller, Fabric Mesh e Edge Components

## Em uma frase
OpenZiti é uma plataforma open-source de rede Zero Trust (Apache-2.0) composta por Controller central, roteadores em malha inteligente (Fabric Mesh) e clientes de borda via SDKs ou Tunnelers.

## Por que importa
Engenharias de segurança substituem VPNs corporativas amplas por segmentação no nível de aplicação onde cada conexão exige autenticação mútua X.509, autorização prévia e criptografia ponta a ponta via `libsodium`.

## Como funciona
O **OpenZiti Controller** coordena identidades, PKI, configurações e políticas de acesso, emitindo sessões autorizadas apenas após validar certificados de cliente e postura. Os **OpenZiti Routers** formam uma malha overlay roteada por latência com failover automático, enquanto **Edge Clients** conectam aplicações diretamente via SDK ou sem alterar código via *tunnelers* locais.

## Exemplo
```bash
# Inicializar uma malha OpenZiti local de avaliação e listar os componentes ativos
ziti edge quickstart \
  --ctrl-address 127.0.0.1 \
  --ctrl-port 1280 \
  --router-address 127.0.0.1 \
  --router-port 3022

ziti edge list edge-routers
ziti edge list services
```

## Limites e trade-offs
Em implantações de produção, o plano de controle do Controller não deve compartilhar a mesma superfície pública não filtrada dos Edge Routers; separe as interfaces `edge-management` e `edge-client` em listeners distintos.

## Como verificar
Execute `ziti edge list edge-routers` e `ziti fabric list links` e confirme que os roteadores estabeleceram links de malha ativos (`Connected`) sob controle do Controller.

## Conexões
- [[ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric]] — Veja também: OpenZiti: Dark Services e Dark Routers sem Portas de Escuta Inbound Expostas.
- [[ziti-identities-enrollment-jwt-ott-certificados-x509-mutuos]] — Referência cruzada direta com ziti-identities-enrollment-jwt-ott-certificados-x509-mutuos.
- [[ziti-politicas-service-policies-edge-router-policies-bind-dial]] — Referência cruzada direta com ziti-politicas-service-policies-edge-router-policies-bind-dial.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.

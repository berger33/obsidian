---
id: software.seguranca.tranche04.000306
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

# OpenZiti: Tunnelers (`ziti-edge-tunnel`) com Interceptação DNS/TPROXY (`intercept.v1`) e Hosting (`host.v1`)

## Em uma frase
O `ziti-edge-tunnel` (e os Ziti Desktop/Mobile Edge) integra aplicações sem modificação de código à malha OpenZiti usando configurações estruturadas `intercept.v1` (lado cliente) e `host.v1` (lado servidor).

## Por que importa
Permite migrar bancos de dados, servidores SSH e APIs legadas para arquitetura *dark* imediatamente, interceptando nomes DNS fictícios ou IPs CGNAT (`100.64.0.0/10`) de forma transparente para o usuário.

## Como funciona
O administrador cria um config `intercept.v1` definindo o endereço virtual (ex.: `db.internal.ziti:5432`) e um config `host.v1` apontando para o destino real (`127.0.0.1:5432`) no servidor. O `ziti-edge-tunnel` do cliente registra um resolvedor DNS local para `*.ziti`, intercepta os pacotes via interface `tun`/TPROXY e os encapsula na malha até o `ziti-edge-tunnel` hospedeiro.

## Exemplo
```bash
# Criar configurações intercept.v1 e host.v1 e associá-las a um serviço OpenZiti
ziti edge create config "pg-intercept-cfg" intercept.v1 \
  '{"protocols":["tcp"],"addresses":["postgres.corp.ziti"],"portRanges":[{"low":5432,"high":5432}]}'

ziti edge create config "pg-host-cfg" host.v1 \
  '{"protocol":"tcp","address":"127.0.0.1","port":5432}'

ziti edge create service "corp-postgres" \
  --configs "pg-intercept-cfg,pg-host-cfg" \
  --encryption ON
```

## Limites e trade-offs
Se o `systemd-resolved` ou gerenciador de DNS corporativo não encaminhar consultas do domínio interceptado para o nameserver local do `ziti-edge-tunnel` (`100.64.0.2`), os clientes falharão com `NXDOMAIN`.

## Como verificar
Execute `ziti-edge-tunnel tunnel_status` e teste `dig postgres.corp.ziti` no host cliente, confirmando a resolução para um IP da faixa `100.64.x.x` e conectividade TCP na porta 5432.

## Conexões
- [[ziti-sdks-application-embedded-zero-trust-go-c-python-jvm]] — Veja também: OpenZiti: SDKs Application-Embedded Zero Trust (Go, C, Python, JVM e Node.js).
- [[ziti-criptografia-ponta-a-ponta-libsodium-kx-chacha20-poly1305]] — Veja também: OpenZiti: Criptografia Ponta a Ponta (`libsodium` Curve25519 / ChaCha20-Poly1305) Acima do mTLS.
- [[ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric]] — Referência cruzada direta com ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric.
- [[ziti-politicas-service-policies-edge-router-policies-bind-dial]] — Referência cruzada direta com ziti-politicas-service-policies-edge-router-policies-bind-dial.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.

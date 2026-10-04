---
id: software.seguranca.tranche04.000305
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

# OpenZiti: SDKs Application-Embedded Zero Trust (Go, C, Python, JVM e Node.js)

## Em uma frase
Os SDKs do OpenZiti permitem embutir a pilha de rede Zero Trust diretamente no código-fonte de clientes e servidores, substituindo sockets TCP dependentes do sistema operacional por conexões virtuais autenticadas sobre a malha.

## Por que importa
Elimina completamente a exposição do serviço na pilha de rede local (`localhost` ou LAN): nem mesmo processos maliciosos rodando na mesma máquina virtual conseguem conectar-se ao servidor sem uma identidade OpenZiti válida.

## Como funciona
No Go SDK (`github.com/openziti/sdk-golang`), o servidor inicializa um contexto com seu arquivo de identidade JSON e chama `zitiContext.Listen("service-name")` em vez de `net.Listen("tcp", ":8080")`, enquanto o cliente chama `zitiContext.Dial("service-name")`, estabelecendo criptografia ponta a ponta (`libsodium`) diretamente entre os processos.

## Exemplo
```go
package main

import (
	"net/http"
	"github.com/openziti/sdk-golang/ziti"
)

func main() {
	cfg, _ := ziti.NewConfigFromFile("/etc/ziti/server-identity.json")
	ctx, _ := ziti.NewContext(cfg)
	listener, _ := ctx.Listen("internal-vault-service")
	_ = http.Serve(listener, http.DefaultServeMux)
}
```

## Limites e trade-offs
Aplicações de terceiros de código fechado (como bancos de dados comerciais ou binários legados) não podem ser recompiladas com o SDK; nesses casos, utilize `ziti-edge-tunnel` em modo `host` no mesmo pod ou VM.

## Como verificar
Inspecione `lsof -i -P -n -p <PID>` do binário compilado com o SDK OpenZiti e verifique que não há nenhum descritor `TCP LISTEN`, existindo apenas conexões `ESTABLISHED` de saída para os Edge Routers.

## Conexões
- [[ziti-politicas-service-policies-edge-router-policies-bind-dial]] — Veja também: OpenZiti: Modelo de Autorização com Service Policies (`Bind`/`Dial`) e Attribute Roles.
- [[ziti-tunnelers-ziti-edge-tunnel-intercept-host-tproxy-dns]] — Veja também: OpenZiti: Tunnelers (`ziti-edge-tunnel`) com Interceptação DNS/TPROXY (`intercept.v1`) e Hosting (`host.v1`).
- [[ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric]] — Referência cruzada direta com ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric.
- [[ziti-criptografia-ponta-a-ponta-libsodium-kx-chacha20-poly1305]] — Referência cruzada direta com ziti-criptografia-ponta-a-ponta-libsodium-kx-chacha20-poly1305.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.

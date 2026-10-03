---
id: software.seguranca.tranche04.000303
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

# OpenZiti: Identidades, Enrollment via One-Time Token (OTT) JWT e mTLS X.509

## Em uma frase
O processo de *enrollment* no OpenZiti provisiona identidades criptográficas fortes usando tokens JWT de uso único (*One-Time Token* — OTT), PKI corporativa de terceiros (*3rd Party CA*) ou provedores OIDC externos.

## Por que importa
Impede o compartilhamento de credenciais estáticas: o JWT de matrícula expira rapidamente e é consumido uma única vez para assinar um CSR gerado localmente cuja chave privada nunca sai do dispositivo.

## Como funciona
O administrador cria a identidade (`ziti edge create identity`) com atributos de papel (`-a`), gerando um arquivo `.jwt` temporário. O endpoint executa `ziti-edge-tunnel enroll` (ou o SDK), gera seu par de chaves localmente, submete um CSR ao Controller apresentando o OTT e recebe o certificado X.509 operacional.

## Exemplo
```bash
# Criar identidade de workload com atributos de role e matricular em arquivo JSON
ziti edge create identity service "payments-worker-01" \
  -a "payments-hosts,prod-workloads" \
  -o /tmp/payments-worker-01.jwt

ziti-edge-tunnel enroll \
  --jwt /tmp/payments-worker-01.jwt \
  --identity /etc/ziti/identities/payments-worker-01.json
```

## Limites e trade-offs
Se um arquivo `.jwt` de matrícula expirar antes do provisionamento da máquina virtual ou pod, a tentativa de enrollment falhará; automatize a emissão *just-in-time* via API REST do Controller ou use auto-enrollment via 3rd Party CA.

## Como verificar
Execute `ziti edge list identities 'name="payments-worker-01"'` e valide que o campo `hasApiSession` ou o estado de enrollment passou a concluído e que o arquivo `.jwt` não pode ser reutilizado.

## Conexões
- [[ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric]] — Veja também: OpenZiti: Dark Services e Dark Routers sem Portas de Escuta Inbound Expostas.
- [[ziti-politicas-service-policies-edge-router-policies-bind-dial]] — Veja também: OpenZiti: Modelo de Autorização com Service Policies (`Bind`/`Dial`) e Attribute Roles.
- [[ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge]] — Referência cruzada direta com ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge.
- [[ziti-posture-checks-mfa-os-process-mac-domain-avaliacao-continua]] — Referência cruzada direta com ziti-posture-checks-mfa-os-process-mac-domain-avaliacao-continua.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.

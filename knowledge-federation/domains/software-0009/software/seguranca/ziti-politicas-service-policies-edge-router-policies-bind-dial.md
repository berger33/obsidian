---
id: software.seguranca.tranche04.000304
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

# OpenZiti: Modelo de Autorização com Service Policies (`Bind`/`Dial`) e Attribute Roles

## Em uma frase
O modelo de políticas do OpenZiti desacopla quem pode consumir um serviço (`Dial`), quem pode hospedá-lo (`Bind`) e quais roteadores de borda cada identidade ou serviço pode atravessar.

## Por que importa
Garante o princípio de privilégio mínimo com escalabilidade operacional: novas identidades e serviços herdam permissões automaticamente através de atributos (`#tag`) em vez de ACLs baseadas em sub-redes IP.

## Como funciona
Quatro tipos de políticas governam a malha: `service-policy` (`Dial` ou `Bind`), `edge-router-policy` (quais identidades acessam quais roteadores) e `service-edge-router-policy` (quais roteadores transportam quais serviços). O operador `Semantic` (`AllOf` vs `AnyOf`) controla se a identidade precisa possuir todos os atributos listados ou apenas um.

## Exemplo
```bash
# Autorizar identidades #sre-team a discar (Dial) para serviços #prod-k8s-apis
ziti edge create service-policy "sre-dial-prod-k8s" Dial \
  --identity-roles "#sre-team" \
  --service-roles "#prod-k8s-apis" \
  --semantic AllOf

# Autorizar os hosts #k8s-control-plane a hospedar (Bind) os serviços #prod-k8s-apis
ziti edge create service-policy "nodes-bind-prod-k8s" Bind \
  --identity-roles "#k8s-control-plane" \
  --service-roles "#prod-k8s-apis"
```

## Limites e trade-offs
Criar uma `service-policy` sem configurar `edge-router-policy` e `service-edge-router-policy` correspondentes impede o estabelecimento do circuito porque não haverá roteador em comum autorizado.

## Como verificar
Execute `ziti edge policy-advisor services -q` ou `ziti edge policy-advisor identities -q` e confirme que a matriz exibe `OK : Common routers > 0` para os pares `Dial` e `Bind` desejados.

## Conexões
- [[ziti-identities-enrollment-jwt-ott-certificados-x509-mutuos]] — Veja também: OpenZiti: Identidades, Enrollment via One-Time Token (OTT) JWT e mTLS X.509.
- [[ziti-sdks-application-embedded-zero-trust-go-c-python-jvm]] — Veja também: OpenZiti: SDKs Application-Embedded Zero Trust (Go, C, Python, JVM e Node.js).
- [[ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge]] — Referência cruzada direta com ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge.
- [[ziti-posture-checks-mfa-os-process-mac-domain-avaliacao-continua]] — Referência cruzada direta com ziti-posture-checks-mfa-os-process-mac-domain-avaliacao-continua.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.

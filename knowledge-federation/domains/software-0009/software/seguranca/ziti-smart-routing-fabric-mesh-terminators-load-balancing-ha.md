---
id: software.seguranca.tranche04.000309
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

# OpenZiti: Smart Routing na Fabric Mesh, Terminators, Custos Dinâmicos e Alta Disponibilidade

## Em uma frase
A malha (*Fabric*) do OpenZiti mede continuamente a latência de cada link entre roteadores e o custo de cada *Terminator*, roteando novos fluxos pelo caminho de menor custo e redirecionando tráfego automaticamente em caso de falha.

## Por que importa
Permite balanceamento de carga ativo-ativo ou failover ativo-passivo na camada de rede Zero Trust sem necessidade de balanceadores L4 externos expostos na internet.

## Como funciona
Múltiplas instâncias de um serviço registrando `Bind` criam múltiplos *Terminators* para o mesmo serviço lógico, cada um com precedência (`default`, `required`, `failed`) e custo base configurável. O Controller calcula o grafo de menor custo somando a latência de cada link de malha e o custo do *Terminator* de destino.

## Exemplo
```bash
# Inspecionar links da malha com latência medida e listar custos dos terminators
ziti fabric list links
ziti fabric list terminators

# Ajustar precedência de um terminator secundário para failover (cost mais alto)
ziti edge update terminator <terminator-id> \
  --precedence default \
  --cost 250
```

## Limites e trade-offs
Conexões TCP já estabelecidas que atravessam um roteador intermediário que cai abruptamente precisarão ser reconectadas pelo SDK/tunneler no novo caminho calculado pela malha.

## Como verificar
Derrube uma instância hospedeira de um serviço com dois *Terminators* ativos e verifique em `ziti edge list terminators` que o tráfego subsequente é encaminhado integralmente para o *Terminator* sobrevivente.

## Conexões
- [[ziti-posture-checks-mfa-os-process-mac-domain-avaliacao-continua]] — Veja também: OpenZiti: Posture Checks Contínuos (OS, Processos, MAC, Domínio e MFA TOTP).
- [[ziti-operacao-kubernetes-helm-ziti-controller-router-zrok-browzer]] — Veja também: OpenZiti: Implantação em Kubernetes via Helm, `ziti-host` para ClusterIPs, `zrok` e BrowZer.
- [[ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge]] — Referência cruzada direta com ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge.
- [[ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric]] — Referência cruzada direta com ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.

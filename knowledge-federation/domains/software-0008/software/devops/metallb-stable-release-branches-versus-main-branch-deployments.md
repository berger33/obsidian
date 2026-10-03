---
id: software.devops.tranche05.000449
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/metallb/metallb/main/README.md", "https://metallb.io/concepts/", "https://github.com/metallb/metallb"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Governança de implantação do MetalLB: uso obrigatório de releases estáveis em vez da branch main

## Em uma frase
O README oficial do MetalLB dedica uma seção inteira intitulada `# WARNING` para alertar os operadores de plataforma: embora a branch `main` tenha sido relativamente estável no passado, ela é a **branch de desenvolvimento ativo**; consumir manifestos ou imagens diretamente da `main` pode resultar em **implantações instáveis ou sem compatibilidade retroativa (non backward compatible deployments)**. Os mantenedores recomendam fortemente consumir sempre uma **branch/release estável**, conforme documentado no guia oficial de instalação (`metallb.io/installation/`).

## Por que importa
Como o MetalLB controla o caminho de entrada de rede de todo o cluster bare-metal (via CRDs, webhooks de validação, sessões BGP e anúncios ARP), aplicar um manifesto em desenvolvimento da branch `main` pode introduzir mudanças de schema nos CRDs ou regressões no daemon `speaker` que derrubam a conectividade externa do cluster.

## Como funciona
Nos seus fluxos GitOps (Argo CD, Flux) ou instalações via Helm/Kustomize, fixe sempre uma tag de release semântica oficial do MetalLB (por exemplo `v0.14.x`) e teste novas releases em um cluster de homologação antes de promovê-las para produção.

## Exemplo
Ao revisar um pull request de infraestrutura que apontava o Kustomize remoto para `github.com/metallb/metallb//config/native?ref=main`, o arquiteto solicita a fixação explícita na tag estável homologada, seguindo o alerta oficial do README.

## Limites e trade-offs
Nunca referencie `ref=main` ou tags `:latest` / `:main` para os contêineres `controller` e `speaker` do MetalLB em manifestos de produção.

## Como verificar
Verifique as tags das imagens em execução em `kubectl -n metallb-system get deploy,ds -o wide` e confirme que correspondem a uma versão oficial estável lançada pelo projeto.

## Conexões
- [[metallb-ip-pool-reassignment-and-service-ip-persistence]] — Veja também: Persistência de IPs atribuídos a Services e reatribuição automática após edição de IPAddressPool.
- [[metallb-security-disclosure-and-48h-response-target]] — Veja também: Reporte de vulnerabilidades de segurança e meta de resposta inicial em 48 horas no MetalLB.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.

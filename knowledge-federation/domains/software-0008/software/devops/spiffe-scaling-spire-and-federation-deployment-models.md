---
id: software.devops.tranche05.000477
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
fontes: ["https://raw.githubusercontent.com/spiffe/spire/main/README.md", "https://spiffe.io/spire/try/", "https://github.com/spiffe/spire"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Escalabilidade e modelos de implantação do SPIRE (doc/scaling_spire.md) e federação de Trust Domains

## Em uma frase
Na seção *Further Reading*, o README oficial referencia o guia **`doc/scaling_spire.md`** (*The Scaling SPIRE guide*), que detalha diretrizes de dimensionamento, recomendações de arquitetura e modelos de implantação para operar o SPIRE em larga escala, bem como a documentação de comparação arquitetural (`spiffe.io/spire/comparisons/`) e o livro oficial gratuito **"Solving the Bottom Turtle"** (`spiffe.io/book/`). Em ambientes multi-cluster ou multi-região, o SPIRE permite tanto topologias com servidores agrupados em alta disponibilidade quanto **federação entre múltiplos Trust Domains** (`spiffe://cluster-a.corp` e `spiffe://cluster-b.corp`), trocando automaticamente os *trust bundles* públicos entre domínios independentes.

## Por que importa
Colocar um único `spire-server` para atender dezenas de milhares de nós através de links WAN intercontinentais cria um domínio de falha global excessivo; já federar múltiplos Trust Domains regionais isola falhas por região ou ambiente enquanto permite mTLS cross-cluster seguro.

## Como funciona
Consulte `doc/scaling_spire.md` para dimensionar o banco de dados do `spire-server`, o TTL dos SVIDs (que determina a taxa de renovação por segundo) e o modelo de federação de Trust Domains entre clusters de produção, staging e parceiros.

## Exemplo
Dois clusters Kubernetes em regiões distintas operam seus próprios `spire-servers` com os domínios `spiffe://sa-east.corp` e `spiffe://us-east.corp` federados via endpoint HTTPS de bundle; serviços da região Sul autenticam chamadas mTLS para a região Norte sem compartilhar chaves privadas de CA.

## Limites e trade-offs
Ao reduzir o TTL dos SVIDs para poucos minutos em clusters com dezenas de milhares de pods, calcule na fórmula de `doc/scaling_spire.md` a taxa resultante de assinaturas de certificados por segundo exigida da CPU do `spire-server` e do `spire-agent`.

## Como verificar
Monitore as métricas de latência de emissão de SVIDs e renovação de bundles no `spire-server` e `spire-agent` garantindo margem confortável antes do vencimento dos certificados.

## Conexões
- [[spiffe-extensible-plugin-framework-node-and-workload-attestation]] — Veja também: Framework extensível de plugins do SPIRE para atestação de nós, workloads e autoridades certificadoras.
- [[spiffe-cure53-and-cncf-tag-security-audits]] — Veja também: Auditorias independentes de segurança do SPIFFE e SPIRE (Cure53 e CNCF TAG-Security) e reporte privado.

## Fontes
- [SPIRE GitHub — README.md (SPIFFE Runtime Environment, Workload API, SVIDs, Envoy SDS & Security Audits)](https://raw.githubusercontent.com/spiffe/spire/main/README.md) — README oficial do SPIRE (projeto graduado na CNCF sob Apache-2.0) detalhando implementação de produção do SPIFFE, SPIFFE Workload API, emissão de SPIFFE IDs e SVIDs (X.509 mTLS e JWT), imagens spire-server/spire-agent/oidc-discovery-provider, bibliotecas go-spiffe e java-spiffe, integração com Envoy SDS, framework de plugins e auditorias de segurança Cure53 (2021) e CNCF TAG-Security (2018 e 2020).; consultado em 2026-10-03.
- [SPIFFE & SPIRE Official Documentation — Quickstart Guides & Architecture](https://spiffe.io/spire/try/) — Portal oficial do SPIFFE e SPIRE com arquitetura de atestação de nó e workload, guias para Kubernetes/Linux/macOS e o livro gratuito Solving the Bottom Turtle.; consultado em 2026-10-03.
- [SPIRE — Official GitHub Repository](https://github.com/spiffe/spire) — Repositório oficial Apache-2.0 do SPIRE na CNCF.; consultado em 2026-10-03.

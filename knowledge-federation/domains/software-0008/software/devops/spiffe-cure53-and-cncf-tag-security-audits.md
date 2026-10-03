---
id: software.devops.tranche05.000478
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

# Auditorias independentes de segurança do SPIFFE e SPIRE (Cure53 e CNCF TAG-Security) e reporte privado

## Em uma frase
A seção *Security* do README oficial documenta o histórico de auditorias formais de segurança do projeto: a empresa independente **Cure53** concluiu uma auditoria profunda de segurança do SPIFFE e do SPIRE em fevereiro de 2021 (`doc/cure53-report.pdf` e post *Scrutinizing SPIRE to Sensibly Strengthen SPIFFE Security*), somando-se às duas avaliações conduzidas pelo **CNCF Technical Advisory Group for Security (TAG-Security / SIG-Security)** em 2018 e 2020 (com modelo de ameaças completo publicado no repositório `cncf/sig-security`). Eventuais vulnerabilidades encontradas devem ser reportadas de forma privada para **`security@spiffe.io`**.

## Por que importa
Como o SPIRE atua literalmente como a raiz de identidade criptográfica de todas as cargas de trabalho do ambiente (a "tartaruga de baixo"), auditores internos e equipes de segurança exigem evidências públicas de revisão criptográfica independente e modelagem de ameaças formal antes de aprová-lo em produção.

## Como funciona
Utilize o relatório da Cure53 (`doc/cure53-report.pdf`) e a avaliação de modelo de ameaças da CNCF SIG-Security como referência ao elaborar a arquitetura de hardening do SPIRE na sua organização, e reporte qualquer falha potencial exclusivamente para `security@spiffe.io`.

## Exemplo
Durante o processo de homologação de arquitetura Zero-Trust em um banco digital, a equipe de segurança anexa o relatório de auditoria da Cure53 e o documento de threat model da CNCF ao dossiê de conformidade e aplica as recomendações de isolamento do datastore e chaves do `spire-server`.

## Limites e trade-offs
Nunca exponha as portas de administração ou o datastore do `spire-server` para redes de aplicações gerais, e proteja o socket Unix do `spire-agent` no host com permissões de arquivo apropriadas.

## Como verificar
Verifique que a versão do SPIRE implantada incorpora todas as releases de segurança atuais em `github.com/spiffe/spire/releases`.

## Conexões
- [[spiffe-scaling-spire-and-federation-deployment-models]] — Veja também: Escalabilidade e modelos de implantação do SPIRE (doc/scaling_spire.md) e federação de Trust Domains.
- [[spiffe-comparing-spire-to-secret-stores-iam-and-service-meshes]] — Veja também: Posição arquitetural do SPIRE frente a cofres de segredos, provedores de identidade, motores de política e service meshes.

## Fontes
- [SPIRE GitHub — README.md (SPIFFE Runtime Environment, Workload API, SVIDs, Envoy SDS & Security Audits)](https://raw.githubusercontent.com/spiffe/spire/main/README.md) — README oficial do SPIRE (projeto graduado na CNCF sob Apache-2.0) detalhando implementação de produção do SPIFFE, SPIFFE Workload API, emissão de SPIFFE IDs e SVIDs (X.509 mTLS e JWT), imagens spire-server/spire-agent/oidc-discovery-provider, bibliotecas go-spiffe e java-spiffe, integração com Envoy SDS, framework de plugins e auditorias de segurança Cure53 (2021) e CNCF TAG-Security (2018 e 2020).; consultado em 2026-10-03.
- [SPIFFE & SPIRE Official Documentation — Quickstart Guides & Architecture](https://spiffe.io/spire/try/) — Portal oficial do SPIFFE e SPIRE com arquitetura de atestação de nó e workload, guias para Kubernetes/Linux/macOS e o livro gratuito Solving the Bottom Turtle.; consultado em 2026-10-03.
- [SPIRE — Official GitHub Repository](https://github.com/spiffe/spire) — Repositório oficial Apache-2.0 do SPIRE na CNCF.; consultado em 2026-10-03.

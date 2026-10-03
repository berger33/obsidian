---
id: software.devops.tranche04.000349
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/anchore/grype/main/README.md", "https://oss.anchore.com/docs/guides/vulnerability/getting-started/", "https://github.com/anchore/grype"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Gates de severidade em pipelines CI/CD e distinção entre vulnerabilidades fixed e not-fixed no Grype

## Em uma frase
A saída padrão do Grype classifica cada vulnerabilidade encontrada tanto **por severidade** (`critical`, `high`, `medium`, `low`, `negligible`) quanto **por status de correção** (`fixed`, quando já existe uma versão corrigida na coluna `FIXED-IN`, `not-fixed`, quando ainda não há patch disponível a montante, e `ignored`). O FAQ oficial confirma que o Grype foi projetado para automação em pipelines de CI/CD, permitindo escanear imagens ou SBOMs durante o build e reprovar pipelines com base em limiares de severidade e disponibilidade de correção.

## Por que importa
Reprovar um build por uma vulnerabilidade `Low` sem correção disponível (`not-fixed` em um utilitário base como `busybox`) trava entregas sem oferecer ação imediata ao desenvolvedor, enquanto permitir que uma vulnerabilidade `Critical` ou `High` com patch disponível (`FIXED-IN` preenchido) passe para produção expõe o ambiente a um risco facilmente evitável.

## Como funciona
Configure os gates de CI/CD do Grype para falhar imediatamente o pipeline quando houver vulnerabilidades acima do limiar definido (como `high` ou `critical`), diferenciando nos fluxos de remediação aquelas que já possuem versão `FIXED-IN` (que exigem apenas atualizar a dependência ou imagem base) daquelas `not-fixed` (que exigem mitigação ou substituição do componente).

## Exemplo
Ao escanear uma imagem no pull request, o Grype detecta um CVE `High` com `FIXED-IN` preenchido; o desenvolvedor atualiza a versão do pacote indicada na coluna `FIXED-IN`, reexecuta o build e o gate aprova a mudança.

## Limites e trade-offs
Evite ignorar permanentemente vulnerabilidades que estão em status `not-fixed` hoje sem reavaliá-las periodicamente, pois assim que o mantenedor da distribuição publicar o patch ela mudará para `fixed` nas execuções seguintes.

## Como verificar
Inspecione a coluna `FIXED-IN` e a linha `by status: X fixed, Y not-fixed, Z ignored` na saída do Grype para validar a acionabilidade das correções.

## Conexões
- [[grype-strict-local-privacy-zero-external-telemetry]] — Veja também: Privacidade estrita no Grype: execução 100% local sem envio de dados externos.
- [[grype-private-registries-and-singularity-oci-formats]] — Veja também: Suporte a registros privados e formatos de imagem Docker, OCI e Singularity no Grype.

## Fontes
- [Anchore Grype GitHub — README.md (Features, Ecosystems, EPSS, KEV, Risk Scoring & OpenVEX)](https://raw.githubusercontent.com/anchore/grype/main/README.md) — README oficial do Anchore Grype detalhando varredura de vulnerabilidades em imagens de contêiner, sistemas de arquivos e SBOMs, suporte a pacotes de SO e linguagens, priorização de ameaças e risco com EPSS, KEV e risk scoring, e filtragem/aumento de resultados com OpenVEX.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Grype Getting Started Guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — Guia oficial de início rápido do Grype cobrindo instalação, varredura de imagens (grype alpine:latest), leitura de saída por severidade e status (fixed/not-fixed/ignored), varredura de SBOMs, relatórios JSON (--output json) e FAQ de operação offline e privacidade.; consultado em 2026-10-03.
- [Anchore Grype — Official GitHub Repository](https://github.com/anchore/grype) — Repositório oficial Apache-2.0 do scanner de vulnerabilidades Grype mantido pela Anchore.; consultado em 2026-10-03.

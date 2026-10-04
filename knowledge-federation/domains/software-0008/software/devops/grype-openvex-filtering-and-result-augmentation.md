---
id: software.devops.tranche04.000344
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

# Filtragem e enriquecimento de resultados de scan com suporte a OpenVEX no Grype

## Em uma frase
O Grype possui suporte nativo a **OpenVEX** (`github.com/openvex`) para filtrar e complementar (augment) resultados de varredura de vulnerabilidades, além das opções de filtragem de resultados documentadas em `oss.anchore.com/docs/guides/vulnerability/filter-results/`. Documentos VEX (Vulnerability Exploitability eXchange) permitem registrar declarações estruturadas e auditáveis informando se um determinado produto ou imagem é afetado ou não (`not_affected`) por um CVE específico, por exemplo quando o código vulnerável não está presente no caminho de execução.

## Por que importa
Quando um scanner reporta um CVE em uma biblioteca embutida cujo subcomponente vulnerável nunca é compilado ou invocado pela aplicação, suprimir o alerta com listas opacas sem justificativa prejudica auditorias futuras. Usar declarações OpenVEX mantém o histórico auditável do motivo técnico pelo qual aquela vulnerabilidade foi filtrada (`ignored`).

## Como funciona
Mantenha declarações OpenVEX versionadas em Git e revisadas pela equipe de segurança, passando-as ao Grype durante a varredura no CI para que vulnerabilidades analisadas como não exploráveis no contexto da aplicação sejam contabilizadas como `ignored`.

## Exemplo
Após análise de engenharia confirmar que um CVE específico de uma biblioteca auxiliar não afeta o binário em produção, o time de segurança emite um documento OpenVEX declarando `not_affected` com justificativa técnica e o fornece ao Grype no pipeline.

## Limites e trade-offs
Nunca adicione regras de supressão ou documentos OpenVEX `not_affected` apenas para fazer um build vermelho passar no CI sem antes validar tecnicamente que o caminho de código vulnerável está de fato inalcançável ou mitigado.

## Como verificar
Execute o Grype fornecendo a configuração de filtragem/OpenVEX e confirme no resumo do terminal que a contagem em `by status` reflete os itens movidos para `ignored`.

## Conexões
- [[grype-epss-kev-and-risk-scoring-prioritization]] — Veja também: Priorização de ameaças e risco no Grype com EPSS, KEV e pontuação de risco (risk scoring).
- [[grype-fast-sbom-scanning-and-unix-piping]] — Veja também: Varredura ultrarrápida de SBOMs existentes via grype sbom:arquivo ou pipe Unix.

## Fontes
- [Anchore Grype GitHub — README.md (Features, Ecosystems, EPSS, KEV, Risk Scoring & OpenVEX)](https://raw.githubusercontent.com/anchore/grype/main/README.md) — README oficial do Anchore Grype detalhando varredura de vulnerabilidades em imagens de contêiner, sistemas de arquivos e SBOMs, suporte a pacotes de SO e linguagens, priorização de ameaças e risco com EPSS, KEV e risk scoring, e filtragem/aumento de resultados com OpenVEX.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Grype Getting Started Guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — Guia oficial de início rápido do Grype cobrindo instalação, varredura de imagens (grype alpine:latest), leitura de saída por severidade e status (fixed/not-fixed/ignored), varredura de SBOMs, relatórios JSON (--output json) e FAQ de operação offline e privacidade.; consultado em 2026-10-03.
- [Anchore Grype — Official GitHub Repository](https://github.com/anchore/grype) — Repositório oficial Apache-2.0 do scanner de vulnerabilidades Grype mantido pela Anchore.; consultado em 2026-10-03.

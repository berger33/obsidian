---
id: software.testes.tranche18.001244
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://trivy.dev/latest/docs/", "https://github.com/aquasecurity/trivy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: registrar exceções com validade

## Em uma frase
Achados podem ser ignorados por arquivo de configuração com identificadores e, quando suportado, prazo de expiração e justificativa.

## Por que importa
Exceções com prazo evitam que riscos aceitos se tornem permanentes por esquecimento e mantêm o histórico da decisão.

## Como funciona
Registre a exceção com identificador do achado, motivo e validade, e revise as exceções periodicamente.

## Exemplo
Uma vulnerabilidade sem correção disponível pode ser aceita por prazo enquanto o fornecedor publica atualização.

## Limites e trade-offs
Exceções amplas por pacote escondem achados novos, e prazos vencidos precisam falhar a verificação em vez de passar silenciosamente.

## Como verificar
Aprove uma exceção com validade vencida e confirme que a ferramenta volta a reportar o achado.

## Conexões
- [[trivy-sbom]] — Veja também: Trivy: gerar e consumir inventário de software.
- [[trivy-ci-policy]] — Veja também: Trivy: definir política no pipeline.

## Fontes
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
- [Trivy — repositório oficial](https://github.com/aquasecurity/trivy) — código-fonte, alvos suportados e documentação do projeto; consultado em 2026-10-03.

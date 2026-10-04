---
id: software.testes.tranche18.001245
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
fontes: ["https://trivy.dev/latest/docs/scanner/vulnerability/", "https://trivy.dev/latest/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: definir política no pipeline

## Em uma frase
A execução pode falhar por código de saída a partir de gravidade mínima ou de achados encontrados, com filtros de severidade e de correção disponível.

## Por que importa
A política precisa equilibrar detecção e ruído, considerando a frequência de atualização das bases de vulnerabilidades.

## Como funciona
Comece bloqueando gravidade alta com correção disponível, reporte o restante e ajuste o critério conforme o passivo se estabiliza.

## Exemplo
Um trabalho de publicação pode ser interrompido por vulnerabilidade crítica corrigível, enquanto achados sem correção são registrados.

## Limites e trade-offs
Bloquear por toda gravidade média gera interrupções frequentes sem ação possível, e nunca bloquear esvazia a verificação.

## Como verificar
Reduza o limite de bloqueio a um valor que o artefato atual viola e confirme que o trabalho falha como previsto.

## Conexões
- [[trivy-ignore-and-baseline]] — Veja também: Trivy: registrar exceções com validade.
- [[trivy-formats-and-output]] — Veja também: Trivy: escolher formato de saída.

## Fontes
- [Trivy — Vulnerability scanning](https://trivy.dev/latest/docs/scanner/vulnerability/) — análise de imagens e sistemas de arquivos por vulnerabilidades; consultado em 2026-10-03.
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.

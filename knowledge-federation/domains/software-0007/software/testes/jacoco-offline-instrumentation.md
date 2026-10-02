---
id: software.testes.tranche15.000895
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/offline.html", "https://www.jacoco.org/jacoco/trunk/doc/agent.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: avaliar a instrumentação offline

## Em uma frase
Na instrumentação offline, as classes são transformadas antes da execução e os dados são gravados pela biblioteca de runtime, sem agente anexado à JVM.

## Por que importa
Alguns ambientes não permitem agente ou exigem artefato já instrumentado, mas o caminho offline muda o fluxo de build e a reprodutibilidade dos artefatos.

## Como funciona
Use offline apenas quando o agente for inviável, mantenha o passo de instrumentação separado do empacotamento de produção e documente o procedimento no pipeline.

## Exemplo
O goal de instrumentação pode gerar uma árvore de classes instrumentadas a partir do diretório de saída do compilador, consumida depois pelos testes.

## Limites e trade-offs
Classes instrumentadas não devem ser publicadas como artefato normal, e misturar artefatos instrumentados com não instrumentados produz medições inconsistentes.

## Como verificar
Compare a medição de uma mesma suíte com agente e com instrumentação offline e verifique se os totais convergem para a mesma execução.

## Conexões
- [[jacoco-check-rules-limits]] — Veja também: JaCoCo: verificar cobertura com regras.
- [[jacoco-merge-exec-files]] — Veja também: JaCoCo: consolidar arquivos de execução.

## Fontes
- [JaCoCo — Offline instrumentation](https://www.jacoco.org/jacoco/trunk/doc/offline.html) — instrumentação fora do processo e diferenças em relação ao agente; consultado em 2026-10-02.
- [JaCoCo — Java agent](https://www.jacoco.org/jacoco/trunk/doc/agent.html) — instrumentação em tempo de execução, opções do agente e arquivo de execução; consultado em 2026-10-02.

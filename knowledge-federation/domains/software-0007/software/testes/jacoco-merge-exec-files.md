---
id: software.testes.tranche15.000896
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
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/agent.html", "https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: consolidar arquivos de execução

## Em uma frase
Quando a suíte roda em várias JVMs, cada processo gera dados próprios, e o goal de merge combina os arquivos em um único conjunto antes do relatório.

## Por que importa
Medir apenas um processo subestima a cobertura real de suítes paralelas e faz a verificação reprovar código que os testes efetivamente exercitaram em outro trabalhador.

## Como funciona
Faça cada processo gravar em um arquivo distinto e consolide os resultados antes de gerar relatório e aplicar a regra de cobertura.

## Exemplo
Um pipeline com quatro executores paralelos pode publicar quatro arquivos de execução e uma etapa de merge produz o `jacoco.exec` usado pelos goals seguintes.

## Limites e trade-offs
A fusão não elimina dados obsoletos de execuções anteriores; arquivos antigos no mesmo diretório precisam ser limpos para não inflar a medição.

## Como verificar
Rode a suíte em dois processos, mescle os arquivos e compare os totais com a soma das partes; em seguida, repita sem limpar e observe o efeito do resíduo.

## Conexões
- [[jacoco-offline-instrumentation]] — Veja também: JaCoCo: avaliar a instrumentação offline.
- [[jacoco-excludes-filtering]] — Veja também: JaCoCo: excluir código gerado da medição.

## Fontes
- [JaCoCo — Java agent](https://www.jacoco.org/jacoco/trunk/doc/agent.html) — instrumentação em tempo de execução, opções do agente e arquivo de execução; consultado em 2026-10-02.
- [JaCoCo — jacoco:report](https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html) — formatos de relatório, fontes, agregação e configuração do goal; consultado em 2026-10-02.

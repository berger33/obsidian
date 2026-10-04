---
id: software.testes.tranche15.000899
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
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/agent.html", "https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: integrar a medição ao ciclo de build

## Em uma frase
A integração típica encadeia preparação do agente, execução dos testes, geração de relatório e verificação, cada passo dependendo do anterior no ciclo do projeto.

## Por que importa
Ordem e escopo incorretos produzem relatório sem dados ou verificação sobre medição incompleta, criando falsa confiança no indicador publicado.

## Como funciona
Vincule cada goal à fase correta, garanta que a verificação ocorra depois da fusão e da geração e mantenha a configuração versionada junto do projeto.

## Exemplo
Em projetos Maven, a configuração costuma usar `prepare-agent` na inicialização, `report` e `check` ao final do ciclo de vida de testes.

## Limites e trade-offs
A ferramenta é agnóstica ao conteúdo dos testes; passar no limite não significa que os cenários cobrem riscos, e a configuração de build não substitui revisão de casos.

## Como verificar
Execute o ciclo completo em um projeto de exemplo e confirme que a falha de verificação interrompe o build no ponto esperado, com relatório disponível para consulta.

## Conexões
- [[jacoco-thresholds-policy]] — Veja também: JaCoCo: tratar cobertura como política, não como meta.

## Fontes
- [JaCoCo — Java agent](https://www.jacoco.org/jacoco/trunk/doc/agent.html) — instrumentação em tempo de execução, opções do agente e arquivo de execução; consultado em 2026-10-02.
- [JaCoCo — jacoco:check](https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html) — regras, elementos, limites, ratios e controle de falha do build; consultado em 2026-10-02.

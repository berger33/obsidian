---
id: software.testes.tranche15.000894
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
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html", "https://www.jacoco.org/jacoco/trunk/doc/counters.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: verificar cobertura com regras

## Em uma frase
O goal de verificação avalia regras compostas por elemento, contador, valor e limite, e pode interromper o build quando o mínimo configurado não é atingido.

## Por que importa
Transformar o limite em guarda automática impede regressões silenciosas, mas regras mal calibradas produzem bloqueios que a equipe aprende a contornar.

## Como funciona
Declare regras por elemento e contador com limites, inicie com valores alcançáveis e trate exceções de forma explícita e revisada.

## Exemplo
Uma regra pode exigir 80% de instruções no pacote e 70% de ramos por classe, enquanto outra impede classes totalmente não cobertas.

## Limites e trade-offs
O padrão de elemento é o pacote e o padrão de contador é instruções; limites máximos existem, mas uso de cobertura como meta pode incentivar testes superficiais.

## Como verificar
Introduza uma classe sem teste e confirme que a verificação falha; depois exclua deliberadamente a regra e verifique se o build volta a passar, registrando a decisão.

## Conexões
- [[jacoco-report-formats]] — Veja também: JaCoCo: escolher o formato de relatório.
- [[jacoco-offline-instrumentation]] — Veja também: JaCoCo: avaliar a instrumentação offline.

## Fontes
- [JaCoCo — jacoco:check](https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html) — regras, elementos, limites, ratios e controle de falha do build; consultado em 2026-10-02.
- [JaCoCo — Coverage counters](https://www.jacoco.org/jacoco/trunk/doc/counters.html) — definições de instruction, branch, line, complexity, method e class; consultado em 2026-10-02.

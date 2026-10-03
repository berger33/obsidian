---
id: software.testes.tranche17.001077
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://github.com/robotframework/robotframework"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: extrair palavras-chave próprias

## Em uma frase
Palavras-chave definidas pelo time agrupam passos repetidos, aceitam argumentos com valores padrão e podem devolver valores para o caso que as chama.

## Por que importa
Reunir passos em uma palavra-chave nomeada reduz duplicação e cria um vocabulário comum entre pessoas técnicas e de negócio.

## Como funciona
Extraia sequências usadas mais de uma vez, nomeie pela intenção do negócio e declare argumentos com padrões apenas quando fizer sentido.

## Exemplo
Uma palavra-chave de login pode receber credenciais com valor padrão para o usuário comum e devolver o perfil carregado após entrar.

## Limites e trade-offs
Palavras-chave genéricas demais escondem detalhes necessários para diagnosticar falhas, e muitas camadas de chamadas dificultam rastrear o passo que quebrou.

## Como verificar
Introduza uma falha em um passo interno e confirme que o log mostra a hierarquia de chamadas até a palavra-chave responsável.

## Conexões
- [[robot-test-case-syntax]] — Veja também: Robot Framework: escrever casos em formato tabular.
- [[robot-templates-data-driven]] — Veja também: Robot Framework: usar modelos para testes orientados a dados.

## Fontes
- [Robot Framework — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — sintaxe de casos, palavras-chave, variáveis, modelos, etiquetas e relatórios; consultado em 2026-10-03.
- [Robot Framework — repositório oficial](https://github.com/robotframework/robotframework) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.

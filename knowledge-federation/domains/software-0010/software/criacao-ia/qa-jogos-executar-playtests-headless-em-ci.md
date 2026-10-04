---
id: software.criacao_ia.tranche02.000181
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/", "https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# QA de Jogos: executar playtests funcionais headless na pipeline de CI

## Em uma frase
A execução de sessões de jogo sem interface gráfica (*headless*) em pipelines de CI/CD detecta quebras e regressões a cada commit.

## Por que importa
Testar jogos exclusivamente através de testes manuais consome centenas de horas e atrasa a validação de novas mecânicas.

## Como funciona
Compile a engine com flag headless (`-batchmode -nographics` no Unity ou `--headless` no Godot) e execute suítes de teste automatizadas que instanciam cenários e avaliam condições de vitória.

## Exemplo
```bash
# Executando suite de testes de integracao headless no Godot 4 via CI
godot --headless --path . --run-tests --quit-after 60
```

## Limites e trade-offs
Testes headless não avaliam artefatos de renderização gráfica, shaders ou bugs visuais dependentes da GPU.

## Como verificar
Rode o comando de teste em modo headless no terminal e confira se o relatório XML de resultados de teste é gerado com sucesso.

## Conexões
- [[qa-jogos-encapsular-loop-em-ambiente-gymnasium]] — Veja também: IA de Testes: encapsular loop de gameplay como ambiente Farama Gymnasium.
- [[claude-code-validar-testes-antes-do-commit]] — Conexão temática direta com claude-code-validar-testes-antes-do-commit.
- [[qa-jogos-isolar-cenarios-de-regressao-de-gameplay]] — Conexão temática direta com qa-jogos-isolar-cenarios-de-regressao-de-gameplay.

## Fontes
- [Farama Gymnasium Documentation — Environment Creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/) — Guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces). Consulta: 2026-10-04.
- [Unity Test Framework Manual](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html) — Documentação de testes de integração playmode, asserções de física e execução automatizada em ci. Consulta: 2026-10-04.

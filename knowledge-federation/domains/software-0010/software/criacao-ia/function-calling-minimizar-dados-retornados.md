---
id: software.criacao_ia.tranche01.000029
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://platform.openai.com/docs/guides/function-calling", "https://platform.openai.com/docs/guides/structured-outputs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Function calling: minimizar dados retornados

## Em uma frase

Resultado de ferramenta deve conter somente informações necessárias para a continuação da tarefa do modelo.

## Por que importa

Reduzir payload diminui exposição de dados privados e evita que contexto irrelevante contamine respostas posteriores.

## Como funciona

Filtre campos no servidor, aplique política de usuário e remova tokens, endereços e dados pessoais não essenciais antes de retornar.

## Exemplo

A ferramenta retorna se uma missão foi concluída e os objetivos restantes, sem enviar perfil completo do jogador.

## Limites e trade-offs

O modelo pode repetir ou resumir dado retornado; minimização precisa ser acompanhada de política de retenção e interface segura.

## Como verificar

Inspecione logs e tráfego para confirmar que segredos e informações fora do escopo não atravessam a fronteira da ferramenta.

## Conexões
- [[ferramentas-pedir-confirmacao-antes-de-efeitos-externos]] — Ferramentas: pedir confirmação antes de efeitos externos.
- [[ferramentas-testar-excecoes-e-falhas-de-execucao]] — Ferramentas: testar exceções e falhas de execução.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.

---
id: software.criacao_ia.tranche02.000198
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
fontes: ["https://diataxis.fr/explanation/", "https://diataxis.fr/how-to-guides/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Manutenção de Software: documentar breaking changes e guias de migração

## Em uma frase
Guias de migração claros reduzem o atrito de atualização para novas versões de frameworks, APIs e bibliotecas de jogos.

## Por que importa
Atualizações de versão que alteram contratos sem documentação de migração travam equipes inteiras e provocam relutância em atualizar ferramentas.

## Como funciona
Mantenha um documento `MIGRATION.md` registrando métodos removidos, novas assinaturas de métodos e exemplos de código comparando a abordagem antiga (*Before*) com a nova (*After*).

## Exemplo
```markdown
# Guia de Migracao da versao 1.x para 2.0

## Remocao de `GetTargetPawn()`
O metodo `GetTargetPawn()` foi descontinuado em favor da propriedade unificada `TargetActor`.

### Antes (v1.x)
```csharp
Pawn target = aiController.GetTargetPawn();
```

### Depois (v2.0)
```csharp
Actor target = aiController.TargetActor;
```
```

## Limites e trade-offs
Omitir mudanças sutis em valores padrão de propriedades pode introduzir bugs de comportamento silenciosos após a migração.

## Como verificar
Execute os passos do guia de migração em um projeto de teste da versão anterior para certificar a precisão das instruções.

## Conexões
- [[documentacao-explicar-grafos-de-shaders-e-materiais]] — Veja também: Documentação de Arte: detalhar entradas e nós matemáticos de shader graphs.
- [[documentacao-automatizar-validacao-de-links-e-snippets-em-ci]] — Veja também: CI para Documentação: testar snippets de código e validar links quebrados.
- [[diataxis-redigir-guias-how-to-para-tarefas-de-producao]] — Conexão temática direta com diataxis-redigir-guias-how-to-para-tarefas-de-producao.
- [[documentacao-fixar-versoes-e-pre-requisitos]] — Conexão temática direta com documentacao-fixar-versoes-e-pre-requisitos.
- [[claude-code-validar-testes-antes-do-commit]] — Conexão temática direta com claude-code-validar-testes-antes-do-commit.

## Fontes
- [Diátaxis Documentation Framework — Explanation](https://diataxis.fr/explanation/) — Especificação formal do quadrante de explicação, arquitetura conceitual e análise de trade-offs. Consulta: 2026-10-04.
- [Diátaxis Documentation Framework — How-to Guides](https://diataxis.fr/how-to-guides/) — Guia para redação de passos orientados a problemas práticos de produção e trabalho diário. Consulta: 2026-10-04.

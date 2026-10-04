---
id: software.criacao_ia.tranche02.000118
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
fontes: ["https://docs.continue.dev/customize/config", "https://github.com/ollama/ollama/blob/main/docs/api.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Continue.dev: padronizar regras de projeto e system prompts

## Em uma frase
A configuração de prompts de sistema padronizados no diretório do projeto alinha o comportamento do assistente às diretrizes da equipe.

## Por que importa
Diferentes desenvolvedores em um mesmo time precisam receber sugestões com estilos consistentes de nomenclatura e tratamento de exceções.

## Como funciona
Crie um arquivo `.continue/rules/padroes.md` ou configure o campo `systemMessage` no `config.json` do workspace detalhando a versão da linguagem, bibliotecas aprovadas e convenções de testes.

## Exemplo
```markdown
<!-- .continue/rules/padroes.md -->
Sempre utilize funcoes assincronas com async/await em vez de callbacks.
Trate erros explicitamente com blocos try/catch e logs estruturados em JSON.
Nunca sugira alteracoes em bibliotecas legadas listadas no arquivo deprecations.md.
```

## Limites e trade-offs
Regras excessivamente extensas ou contraditórias degradam a aderência do modelo às instruções e consomem espaço da janela de contexto.

## Como verificar
Solicite uma implementação simples ao modelo local e certifique-se de que a estrutura gerada obedece às regras estipuladas no arquivo de padrões.

## Conexões
- [[llamacpp-servir-endpoint-openai-compativel]] — Veja também: llama.cpp: servir endpoint HTTP compatível com OpenAI.
- [[continue-dev-auditar-requisicoes-e-logs-locais]] — Veja também: Continue.dev: auditar requisições e logs de execução local.
- [[cursor-padronizar-regras-com-cursorrules]] — Conexão temática direta com cursor-padronizar-regras-com-cursorrules.
- [[copilot-registrar-instrucoes-do-repositorio]] — Conexão temática direta com copilot-registrar-instrucoes-do-repositorio.
- [[continue-dev-customizar-context-providers]] — Conexão temática direta com continue-dev-customizar-context-providers.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.

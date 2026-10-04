---
id: software.criacao_ia.tranche02.000119
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

# Continue.dev: auditar requisições e logs de execução local

## Em uma frase
A auditoria de logs locais permite inspecionar os prompts reais montados pela extensão e o tempo gasto em cada requisição.

## Por que importa
Inspecionar o conteúdo enviado ajuda a identificar vazamentos de contexto desnecessário e a diagnosticar lentidões na inferência.

## Como funciona
Acesse os arquivos de log no diretório `~/.continue/logs/core.log` ou ative a exibição de saída de depuração no terminal do desenvolvedor para examinar payloads de entrada, tokens gerados e mensagens de erro.

## Exemplo
```bash
# Inspecionar os ultimos prompts e respostas trafegados pelo Continue
tail -f ~/.continue/logs/core.log
```

## Limites e trade-offs
Logs detalhados acumulam dados rapidamente e podem registrar trechos de código privado no disco da máquina local.

## Como verificar
Abra o arquivo de log após executar uma edição com o assistente e verifique os timestamps de requisição e a latência de geração reportada.

## Conexões
- [[continue-dev-padronizar-regras-de-projeto]] — Veja também: Continue.dev: padronizar regras de projeto e system prompts.
- [[ia-local-garantir-isolamento-sem-conexao-externa]] — Veja também: IA Local: garantir isolamento de rede para código sensível.
- [[continue-dev-configurar-provedor-local]] — Conexão temática direta com continue-dev-configurar-provedor-local.
- [[claude-code-iniciar-sessao-interativa-cli]] — Conexão temática direta com claude-code-iniciar-sessao-interativa-cli.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.

---
id: software.criacao_ia.tranche02.000120
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

# IA Local: garantir isolamento de rede para código sensível

## Em uma frase
Configurar o ambiente de desenvolvimento assistido por IA sem conectividade externa assegura conformidade com requisitos de segurança e sigilo.

## Por que importa
Empresas com políticas estritas de proteção de propriedade intelectual exigem que códigos confidenciais nunca saiam da rede interna.

## Como funciona
Configure o firewall do sistema ou container para bloquear tráfego de saída das portas do assistente e dos servidores de modelo (Ollama / llama.cpp), limitando a escuta estritamente a `127.0.0.1`.

## Exemplo
```bash
# Bloquear trafego externo para portas de inferencia local no Linux
sudo iptables -A OUTPUT -p tcp --dport 11434 -d 127.0.0.1 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --dport 11434 -j REJECT
```

## Limites e trade-offs
O isolamento de rede impede a consulta de documentações web dinâmicas e o download automático de novos pesos de modelos via CLI.

## Como verificar
Desconecte a interface de rede externa e execute uma chamada de completude para confirmar que o modelo gera respostas exclusivamente a partir da GPU local.

## Conexões
- [[continue-dev-auditar-requisicoes-e-logs-locais]] — Veja também: Continue.dev: auditar requisições e logs de execução local.
- [[continue-dev-configurar-provedor-local]] — Conexão temática direta com continue-dev-configurar-provedor-local.
- [[llamacpp-servir-endpoint-openai-compativel]] — Conexão temática direta com llamacpp-servir-endpoint-openai-compativel.
- [[ollama-gerenciar-permanencia-com-keep-alive]] — Conexão temática direta com ollama-gerenciar-permanencia-com-keep-alive.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.

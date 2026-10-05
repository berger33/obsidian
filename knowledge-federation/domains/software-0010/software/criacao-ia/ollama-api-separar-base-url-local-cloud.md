---
id: software.criacao_ia.tranche05.000401
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://docs.ollama.com/api/introduction", "https://docs.ollama.com/api/generate"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: diferenciar base URLs local e cloud antes de configurar o cliente

## Em uma frase
O cliente deve selecionar a base URL correspondente ao destino, porque o servidor local e o acesso cloud usam hosts, autenticação e capacidades diferentes.

## Por que importa
Uma aplicação que troca de local para cloud sem mudar a configuração pode enviar credenciais desnecessárias, apontar para o endpoint errado ou supor que operações locais existem na nuvem.

## Como funciona
A documentação lista `http://localhost:11434/api` para a API local e `https://ollama.com/api` para cloud direto; a compatibilidade OpenAI usa `/v1` em ambos os hosts. Cloud direto exige API key, enquanto chamadas locais não exigem essa chave.

## Exemplo
Mantenha `OLLAMA_BASE_URL` configurável por ambiente: desenvolvimento usa `http://localhost:11434/api`, e o serviço cloud usa `https://ollama.com/api` acompanhado do segredo configurado no servidor.

## Limites e trade-offs
A documentação ressalta que criação e remoção de modelos exigem servidor local. Não conclua que todos os endpoints locais estão disponíveis no acesso cloud apenas porque a API de geração tem um host cloud.

## Como verificar
Inspecione host, prefixo de endpoint e política de autenticação da configuração efetiva; faça um teste controlado com o modelo destinado a cada ambiente, sem registrar a chave em logs.

## Conexões
- [[ollama-api-generate-stream-e-done]] — Ollama API: tratar stream de generate até o marcador done.

## Fontes
- [Ollama API — Introduction](https://docs.ollama.com/api/introduction) — Tabela oficial de base URLs, autenticação local/cloud e ressalva sobre operações de gerenciamento locais. Consulta: 2026-10-04.
- [Ollama API — Generate a response](https://docs.ollama.com/api/generate) — Exemplo oficial de endpoint local e corpo de uma operação de geração. Consulta: 2026-10-04.

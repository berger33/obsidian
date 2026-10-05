---
id: software.criacao_ia.tranche05.000409
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
fontes: ["https://docs.ollama.com/api/copy", "https://docs.ollama.com/api/tags"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: copiar um modelo para um nome isolado antes de alterar a configuração

## Em uma frase
`POST /api/copy` recebe nomes `source` e `destination`, permitindo criar uma cópia registrada sob outro nome sem confundir seleção e origem.

## Por que importa
Separar o nome de trabalho do nome de referência torna mais claro qual variante uma aplicação consome e qual configuração está sendo mantida para comparação.

## Como funciona
Confirme que a origem é a esperada, defina explicitamente um nome de destino e trate a resposta de sucesso como conclusão da cópia. Depois consulte `/api/tags` para verificar o novo nome antes de referenciá-lo em configurações.

## Exemplo
Um script de manutenção copia `coder-base` para `coder-experiment-a`, registra origem e destino em um manifesto local e só então atualiza o ambiente de teste para usar o nome novo.

## Limites e trade-offs
A documentação descreve a operação como cópia com nomes distintos; não infira que modelos sob nomes diferentes sejam versões independentes de pesos nem use cópia como mecanismo de backup externo.

## Como verificar
Teste com nomes controlados em uma instalação local, valide a resposta, liste os modelos depois e assegure que o cliente não troca a origem pelo destino por erro de variável.

## Conexões
- [[ollama-api-create-configurar-modelo-derivado]] — Ollama API: criar um modelo derivado com parâmetros e instruções explícitas.
- [[ollama-api-delete-model-protegido]] — Ollama API: proteger a remoção de modelos com confirmação do nome exato.

## Fontes
- [Ollama API — Copy a model](https://docs.ollama.com/api/copy) — Define os campos obrigatórios `source` e `destination` e a resposta de sucesso. Consulta: 2026-10-04.
- [Ollama API — List models](https://docs.ollama.com/api/tags) — Fornece uma verificação posterior do nome de destino no catálogo. Consulta: 2026-10-04.

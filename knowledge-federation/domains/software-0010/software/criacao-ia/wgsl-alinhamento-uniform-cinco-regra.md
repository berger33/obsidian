---
id: software.criacao_ia.tranche04.000313
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://www.w3.org/TR/WGSL/#alignment-and-size", "https://www.w3.org/TR/WGSL/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: o layout de uniform padroniza tudo em 16 bytes

## Em uma frase
No espaço 'uniform', cada membro de uma struct começa em múltiplo do seu próprio alinhamento, com um mínimo de 16, e arrays consomem 16 bytes por elemento quando o tipo base é menor.

## Por que importa
Campos compactados 'na mão' no lado da CPU geram offsets silenciosamente deslocados quando a regra do compilador não é respeitada — um vec3<f32> no fim de um array de uniform consome 16, não 12 bytes, e o shader lê o float errado sem qualquer mensagem de erro.

## Como funciona
Ordene membros do maior alinhamento para o menor (vec4, matNxM antes de scalares), preencha lacunas com pad e evite arrays de tipos de alinhamento 8 dentro de uniform (o array força passo 16). Prefira vec4+mat4x4 para conjuntos pequenos: o desperdício é previsível e o layout, trivial. O storage buffer não tem piso de 16 por membro — lá o custo de alinhar é menor, razão pela qual motores movem blocos grandes para storage.

## Exemplo
Um bloco por-draw { vec4 color; float time; } ocupa 16 bytes (color) + 4 (time) + 12 de preenchimento = 32; o upload com stride 20 é a fonte clássica do bug de 'o time lê lixo'.

## Limites e trade-offs
As regras exatas vêm das tabelas de 'alignment and size' da especificação; implementações as seguem, mas o erro de layout só aparece em validação de binding size se o minBindingSize ajudar — muitas vezes aparece como dado errado, não exceção. Matrices em uniform: colunas alinhadas a 16.

## Como verificar
Calcule o tamanho esperado via um gerador (o próprio JS pode montar a struct espelho) e compare com o size de upload; uma asserção na inicialização pega regressões. Mude um membro para storage e confirme que o layout mudou — sinal de que você entendeu a regra.

## Conexões
- [[wgsl-binding-layout-visibilidade]] — WGSL: pares @group/@binding são contrato com o layout do pipeline.
- [[wgsl-storage-runtime-array]] — WGSL: só o storage buffer aceita array de tamanho em tempo de execução.

## Fontes
- [W3C — WGSL: Alignment and Size](https://www.w3.org/TR/WGSL/#alignment-and-size) — tabelas normativas de alinhamento/tamanho por tipo e por espaço de armazenamento Consulta: 2026-10-04.
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — contexto das restrições por espaço de armazenamento (uniform vs. storage) Consulta: 2026-10-04.

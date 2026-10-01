# Plano de execução — Vault federado de 1 milhão de notas

Data-base: 2026-09-30

## 1. Objetivo

Construir, em várias rodadas, uma biblioteca massiva de conhecimento em formato compatível com Obsidian, com foco em:

1. desenvolvimento de software;
2. inteligência artificial;
3. vibe coding e engenharia agêntica;
4. cannabis medicinal, em abordagem legal, científica, médica, regulatória e de documentação pessoal;
5. micologia, com foco seguro em biologia, taxonomia, histórico, riscos, legislação, pesquisa científica e cultivo legal de cogumelos não controlados como referência técnica.

## 2. Restrição importante de segurança e legalidade

O vault não deve conter instruções operacionais para cultivar, produzir, extrair, otimizar rendimento ou burlar fiscalização de substâncias controladas ou potencialmente ilícitas.

### 2.1 Cannabis medicinal

Conteúdo permitido:

- legislação e regulação;
- documentação de paciente;
- glossário médico e botânico;
- diferenças entre espécies, quimiotipos, fitocanabinoides e terpenos;
- riscos, interações medicamentosas e acompanhamento médico;
- modelos de diário terapêutico;
- checklist de conformidade jurídica;
- revisão de literatura científica;
- boas práticas gerais de segurança, armazenamento legal e rastreabilidade, sem instrução de produção ilícita.

Conteúdo a evitar:

- passo a passo de cultivo;
- parâmetros operacionais para maximizar produção;
- instruções de extração/concentração;
- técnicas de ocultação;
- orientação para contornar lei, fiscalização ou prescrição.

### 2.2 Psilocybe cubensis e psilocibina

Conteúdo permitido:

- taxonomia e história científica;
- legislação por jurisdição;
- riscos, contraindicações, interações e redução de danos em nível educacional;
- pesquisa clínica sobre psilocibina, com fontes acadêmicas;
- diferenças entre cogumelos legais comestíveis/medicinais e espécies controladas;
- micologia geral;
- cultivo legal de espécies não controladas como Pleurotus, Hericium e Agaricus, se for útil para aprender micologia.

Conteúdo a evitar:

- tek, receita, substrato, inoculação, colonização, frutificação ou parâmetros para Psilocybe cubensis;
- otimização de potência, rendimento ou extração;
- instruções para aquisição de esporos, isolamento, clonagem ou distribuição;
- qualquer orientação para produção ilegal.

## 3. Realidade técnica: 1 milhão de notas não deve ser um único vault comum

Um vault único com 1 milhão de arquivos Markdown pode ficar pesado para:

- indexação do Obsidian;
- sincronização;
- Graph View;
- plugins como Dataview;
- busca local;
- Git;
- auditoria de links.

A arquitetura recomendada é um **vault federado**:

```text
knowledge-federation/
  00-home-vault/                 # índice mestre, MOCs globais, árvores de decisão
  domains/
    software-0001/
    software-0002/
    ai-0001/
    vibe-coding-0001/
    cannabis-medicinal-0001/
    micologia-legal-0001/
    ...
  registry/
    notes.sqlite                 # manifesto global
    sources.sqlite               # fontes
    links.sqlite                 # grafo global
    batches.sqlite               # progresso por lote
  exports/
    zips/
    reports/
  scripts/
    generate_batch.py
    audit_batch.py
    build_indexes.py
    build_canvases.py
```

Cada sub-vault deve ter algo como 5.000 a 20.000 notas. O índice mestre aponta para os sub-vaults e mantém MOCs globais.

## 4. Unidade de trabalho: lote pequeno, auditável e retomável

Nunca tentar gerar centenas de milhares de notas em uma única execução.

### Tamanho recomendado de lote

- lote mínimo: 100 notas;
- lote normal: 500 notas;
- lote grande: 1.000 notas;
- lote máximo por execução: 2.000 notas, se a auditoria estiver rápida.

### Checkpoint obrigatório por lote

Cada lote deve gerar:

```text
batch_id
area
subarea
quantidade_planejada
quantidade_gerada
fontes_usadas
notas_criadas
links_criados
links_quebrados
notas_orfas
tempo_inicio
tempo_fim
status
hash_manifesto
relatorio_auditoria
```

Status possíveis:

```text
planned
researching
drafting
auditing
complete
failed
needs_review
```

## 5. Pipeline de execução

### Fase 0 — Taxonomia global

Criar a árvore de domínios, subdomínios e tópicos.

Domínios iniciais:

```text
software/
  fundamentos
  arquitetura
  frontend
  backend
  mobile
  desktop
  dados
  devops
  seguranca
  testes
  produto
  jogos
  sistemas-empresariais
  low-code

ia/
  fundamentos
  llms
  agentes
  rag
  fine-tuning
  modelos-locais
  seguranca
  avaliacao
  custos
  ferramentas

vibe-coding/
  conceitos
  ferramentas
  workflows
  prompts
  context-engineering
  spec-driven-dev
  qualidade
  riscos
  estudos

cannabis-medicinal/
  legal-regulatorio
  paciente-documentacao
  botanica-geral
  farmacologia
  canabinoides
  terpenos
  formas-de-uso-legais
  riscos-e-interacoes
  estudos-clinicos
  glossario

micologia/
  fundamentos
  taxonomia
  ecologia
  cogumelos-comestiveis-legais
  cogumelos-medicinais-legais
  psilocybe-historia-taxonomia-legislacao
  psilocibina-pesquisa-clinica
  riscos-e-reducao-de-danos
  glossario
```

### Fase 1 — Backlog de 1 milhão de notas

Gerar primeiro apenas títulos, slugs, domínio, nível e tipo.

Nada de corpo de nota ainda.

Manifesto mínimo:

```yaml
id: software.backend.api-rest.versionamento-000001
slug: versionamento-de-api-rest
nome: Versionamento de API REST
dominio: software
subdominio: backend
tipo: conceito
nivel: iniciante
status: planned
fontes_minimas: []
risco: baixo
```

### Fase 2 — Pesquisa por domínio

Antes de redigir lotes, registrar fontes primárias.

Ordem de fontes:

1. documentação oficial;
2. papers e relatórios técnicos;
3. livros e materiais acadêmicos;
4. blogs técnicos reconhecidos;
5. opinião de comunidade, sempre marcada como opinião.

### Fase 3 — Redação em lotes

Para cada lote:

1. carregar manifesto do lote;
2. selecionar fontes;
3. gerar notas;
4. criar links mínimos;
5. atualizar MOCs locais;
6. rodar auditoria;
7. salvar relatório;
8. atualizar registry SQLite;
9. compactar sub-vault se necessário.

### Fase 4 — Auditoria incremental

A cada lote:

- links quebrados;
- notas órfãs;
- fontes ausentes;
- frontmatter inválido;
- notas duplicadas;
- slugs duplicados;
- conteúdo proibido/sensível;
- notas longas demais;
- notas com confiança baixa;
- dados voláteis sem data.

### Fase 5 — Índices globais

A cada 10 lotes:

- atualizar Home global;
- atualizar MOCs por domínio;
- atualizar árvores de decisão;
- atualizar canvases;
- atualizar estatísticas.

## 6. Padrão de nota em escala massiva

Para 1 milhão de notas, nem toda nota pode ter 400 palavras. Use três densidades:

### 6.1 Nota semente

100 a 180 palavras.

Uso:

- conceitos de baixa prioridade;
- verbetes;
- nós de ligação.

### 6.2 Nota padrão

200 a 450 palavras.

Uso:

- conceitos centrais;
- ferramentas;
- técnicas;
- comparativos pequenos.

### 6.3 Nota profunda

800 a 1.500 palavras.

Uso:

- MOCs;
- decisões críticas;
- comparativos grandes;
- tópicos legais, médicos, segurança e arquitetura.

## 7. Esquema de IDs

Usar IDs estáveis, independentes do nome do arquivo.

```text
<dominio>.<subdominio>.<topico>.<sequencia>
```

Exemplos:

```text
software.backend.api.versionamento.000001
ia.agentes.mcp.servidores.000001
vibe.contexto.regras-projeto.000001
cannabis.legal.habeas-corpus.000001
micologia.legal.psilocibina-brasil.000001
```

## 8. Frontmatter recomendado

```yaml
---
id: software.backend.api.versionamento.000001
tipo: conceito
dominio: software
subdominio: backend
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: estavel
risco_legal: baixo
risco_medico: baixo
status: semente
fontes: []
tags: [dominio/software, backend/api]
aliases: []
lote: batch-000001
---
```

Para cannabis e psilocibina/cogumelos:

```yaml
risco_legal: medio | alto
risco_medico: medio | alto
conteudo_operacional: false
permitido: educacional | legal | cientifico | medico | historico
```

## 9. Controle para não perder progresso

### 9.1 Persistência a cada lote

Depois de cada lote completo:

- salvar arquivos Markdown;
- atualizar SQLite;
- gerar relatório de auditoria;
- gerar zip do lote;
- atualizar `_meta/progresso.md`;
- registrar changelog.

### 9.2 Persistência dentro do lote

Para lotes acima de 500 notas:

- salvar a cada 50 notas;
- escrever `batch_state.json`;
- permitir retomar do último índice.

Exemplo:

```json
{
  "batch_id": "batch-000123",
  "status": "drafting",
  "last_completed_index": 350,
  "total": 1000,
  "updated_at": "2026-09-30T18:40:00-03:00"
}
```

### 9.3 Execução idempotente

O gerador deve poder rodar duas vezes sem duplicar notas.

Regra:

- se `id` já existe e hash de conteúdo igual, pular;
- se `id` existe e conteúdo mudou, criar revisão;
- se slug existe com outro id, resolver conflito adicionando sufixo.

## 10. Estimativa de volume

Para chegar a 1.000.000 notas:

| Tamanho do lote | Lotes necessários |
|---:|---:|
| 100 notas | 10.000 lotes |
| 500 notas | 2.000 lotes |
| 1.000 notas | 1.000 lotes |
| 2.000 notas | 500 lotes |

Estratégia realista:

- 1ª meta: 10.000 notas úteis;
- 2ª meta: 50.000 notas;
- 3ª meta: 100.000 notas;
- 4ª meta: 250.000 notas;
- 5ª meta: 1.000.000 notas, se a utilidade continuar alta.

## 11. Distribuição inicial sugerida

```text
software: 450.000 notas
ia: 220.000 notas
vibe-coding: 120.000 notas
jogos: 90.000 notas
cannabis-medicinal: 60.000 notas
micologia: 40.000 notas
negocio-carreira-produto: 20.000 notas
```

Observação: jogos pode ser tratado dentro de software ou como domínio próprio.

## 12. Primeiros 20 lotes recomendados

1. software/fundamentos — 500 notas
2. software/backend — 500 notas
3. software/frontend — 500 notas
4. software/arquitetura — 500 notas
5. software/testes — 500 notas
6. ia/fundamentos — 500 notas
7. ia/llms — 500 notas
8. ia/agentes — 500 notas
9. vibe-coding/conceitos — 500 notas
10. vibe-coding/workflows — 500 notas
11. vibe-coding/prompts — 500 notas
12. jogos/engines — 500 notas
13. jogos/netcode — 500 notas
14. cannabis-medicinal/legal-regulatorio — 300 notas
15. cannabis-medicinal/paciente-documentacao — 300 notas
16. cannabis-medicinal/farmacologia — 300 notas
17. micologia/fundamentos — 300 notas
18. micologia/cogumelos-comestiveis-legais — 300 notas
19. micologia/psilocibina-pesquisa-clinica — 300 notas
20. riscos-e-seguranca — 500 notas

Total inicial: aproximadamente 9.000 notas.

## 13. Comandos futuros desejados

Criar CLI interna:

```bash
python scripts/plan_batches.py --target 1000000
python scripts/generate_batch.py --batch batch-000001 --limit 500
python scripts/audit_batch.py --batch batch-000001
python scripts/build_global_indexes.py
python scripts/export_zip.py --vault software-0001
```

## 14. Critérios de parada

Parar o lote e marcar `needs_review` se ocorrer:

- mais de 1% de links quebrados;
- qualquer nota sem frontmatter;
- qualquer conteúdo proibido em cannabis/psilocibina;
- mais de 5% de notas com fonte ausente;
- duplicação de slug acima de 0,5%;
- tempo de auditoria acima de limite definido;
- vault/sub-vault acima do tamanho planejado.

## 15. Próxima ação recomendada

Implementar o sistema de geração federada antes de gerar novos conteúdos em massa:

1. `registry/notes.sqlite`;
2. `scripts/plan_batches.py`;
3. `scripts/generate_seed_manifest.py`;
4. `scripts/generate_batch.py`;
5. `scripts/audit_batch.py`;
6. primeiro lote real de 500 notas.

---
id: software.seguranca.tranche04.000364
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md", "https://docs.projectdiscovery.io/opensource/katana/overview", "https://github.com/projectdiscovery/katana/releases"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Katana: Preenchimento Automático de Formulários (`-aff`, `-fc`), Extração (`-fx`) e Estratégias de Visita (`-s`)

## Em uma frase
O `katana` descobre estados profundos da aplicação extraindo elementos `<form>`, `<input>`, `<textarea>` e `<select>` (`-fx`) e preenchendo formulários automaticamente (`-aff` / `-automatic-form-fill`) com base em regras customizáveis (`-fc` / `form-config.yaml`).

## Por que importa
Muitas rotas e fluxos de negócio só são alcançados após submeter formulários de busca, filtros ou cadastros multi-etapa com valores sintaticamente válidos (e-mail, telefone, CEP, datas).

## Como funciona
O arquivo `form-config.yaml` mapeia expressões regulares sobre atributos `name`, `id`, `placeholder` ou `type` dos inputs HTML para valores de teste adequados. Além disso, a flag `-s` (`-strategy`) alterna a ordem de travessia do grafo de links entre `depth-first` (padrão, aprofundando um fluxo até `-d`) e `breadth-first` (explorando primeiro todas as páginas de nível 1 antes do nível 2).

## Exemplo
```bash
# Executar crawling breadth-first preenchendo formulários e extraindo metadados de inputs no JSONL
katana -u https://portal.staging.corp \
  -s breadth-first -d 3 \
  -aff -fx \
  -fc /etc/katana/custom-form-config.yaml \
  -jsonl -o forms-and-routes.jsonl
```

## Limites e trade-offs
Habilitar `-aff` em sessões autenticadas sem bloquear rotas destrutivas via `-cos` pode submeter formulários de alteração de senha, criação massiva de tickets ou exclusão de registros no ambiente.

## Como verificar
Inspecione `jq -c 'select(.request.method == "POST")' forms-and-routes.jsonl` para auditar os formulários submetidos e os campos descobertos.

## Conexões
- [[katana-controle-escopo-field-scope-crawl-scope-out-of-scope]] — Veja também: Katana: Controle Estrito de Escopo (`-fs`, `-cs`, `-cos`, `-do` e `-e`) para Prevenção de Fuga de Crawl.
- [[katana-deduplicacao-similaridade-fsu-pcs-simhash-tfidf-bm25]] — Veja também: Katana: Deduplicação de URLs Paramétricas (`-fsu`, `-iqp`) e Similaridade de Conteúdo (`-pcs` SimHash/TF-IDF/BM25).
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.

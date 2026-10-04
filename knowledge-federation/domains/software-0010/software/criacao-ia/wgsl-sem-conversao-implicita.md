---
id: software.criacao_ia.tranche04.000320
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
fontes: ["https://www.w3.org/TR/WGSL/", "https://developer.mozilla.org/en-US/docs/Web/API/GPUShaderModule/getCompilationInfo"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: sem coerções implícitas — o construtor é obrigatório e o erro é cedo

## Em uma frase
WGSL não converte scalar↔vetor nem tipo numérico implicitamente; cada conversão (int para float, vec3 para vec4) precisa de um construtor explícito, e literais devem ser digitados.

## Por que importa
Portadores de GLSL e HLSL carregam o hábito de expressões que 'funcionam por mágica'. Em WGSL o compilador recusa, e isso é uma vantagem: a política de precisão e sinal fica visível no código-fonte, onde revisão e testes podem enxergá-la — i32(1.5) truncando é seu bug explícito, não escondido.

## Como funciona
Escreva float(1) ou 1.0 conforme o caso; converta vetores por construtor ('vec4f(pos, 1.0)'); use select() em vez de ternário com ramos de tipo divergente; e para lógica boolean↔numérica prefira if/int(true). Literais sem sufixo assumem o tipo inferido do contexto — anote quando o contexto não basta, para evitar que um i32 de 32 bits vire u32 silencioso num laço. O compilador reporta esses casos como erros de compilação do módulo, legíveis via getCompilationInfo().

## Exemplo
O pós-processador que soma 'luma = dot(albedo.rgb, vec3(0.2126, 0.7152, 0.0722))' escrito em GLSL só compila em WGSL com os literais float coerentes; o diff de migração inteiro é um teste de atenção.

## Limites e trade-offs
getCompilationInfo informa mensagens por 'line' e 'offset' mas o mapeamento de fonte do seu pré-processador de shaders pode embaralhar as posições — mantenha o texto-fonte exato enviado. O erro é na compilação do módulo, antes da criação do pipeline; não espere recuperação por runtime. Ferramentas de validação independentes existem na comunidade, mas não substituem o compilador da plataforma.

## Como verificar
Conecte getCompilationInfo() a um assert da build (testes de shader devem falhar no CI se 'messages' contiver erro para um fixture). Mantenha um 'kitchen sink' shader cobrindo cada padrão de coerção e confirme que só as formas explícitas compilam. Registre a posição reportada vs. real para calibrar o pré-processador.

## Conexões
- [[wgsl-uniformidade-amostragem]] — WGSL: fluxo divergente e operações uniformes — uma análise, não uma sugestão.

## Fontes
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — define regras de conversão explícita, literais e inferência de tipo Consulta: 2026-10-04.
- [MDN — GPUShaderModule/getCompilationInfo()](https://developer.mozilla.org/en-US/docs/Web/API/GPUShaderModule/getCompilationInfo) — documenta o acesso programático a erros e avisos de compilação Consulta: 2026-10-04.
